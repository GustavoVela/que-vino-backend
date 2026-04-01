import logging
from datetime import datetime
import asyncio
from typing import Dict, List
from core import gcs_client, gemini_client, db
from config import settings
import uuid

"""
Servicio de Sincronización de Conocimiento (RAG Sync Service).
Este módulo gestiona la réplica bidireccional (Mirroring) entre Google Cloud Storage 
y Gemini File Search Stores, asegurando que el modelo siempre tenga acceso 
a la versión más reciente de la documentación del proyecto.
"""

def log_sync_action(transaction_id: str, bucket_name: str, store_id: str, file_name: str, action: str, size: int, user_id: str):
    """
    Registra una acción de auditoría de sincronización en BigQuery.
    
    Args:
        transaction_id (str): Identificador único de la sesión de sincronización.
        bucket_name (str): Nombre del bucket origen en GCS.
        store_id (str): ID del repositorio destino en Gemini.
        file_name (str): Nombre del archivo procesado.
        action (str): Acción realizada (UPLOADED, REPLACED, DELETED, ERROR).
        size (int): Tamaño del archivo en bytes.
        user_id (str): ID del usuario que inició la operación.
    """
    now = datetime.utcnow().isoformat() + "Z"
    row = {
        "transaction_id": transaction_id,
        "bucket_name": bucket_name,
        "store_id_gemini": store_id,
        "file_name": file_name,
        "action_taken": action,
        "file_size_bytes": size,
        "performed_by_user_id": user_id,
        "event_timestamp": now,
        "ingestion_timestamp": now
    }
    # Registro asíncrono para no bloquear el flujo de sincronización masiva
    db.log_event_async(settings.bq_dataset_transactions, settings.table_sync_log, row)

async def process_file_sync(
    file_name: str, 
    gcs_size: int, 
    bucket_name: str, 
    store_id: str, 
    user_id: str, 
    transaction_id: str, 
    gemini_dict: Dict, 
    semaphore: asyncio.Semaphore
) -> str:
    """
    Procesa la sincronización de un archivo individual bajo un esquema de concurrencia controlada.
    
    Args:
        file_name (str): Nombre del objeto en GCS.
        gcs_size (int): Tamaño actual en GCS.
        bucket_name (str): Bucket de origen.
        store_id (str): Repositorio Gemini de destino.
        user_id (str): ID del usuario operador.
        transaction_id (str): ID de la transacción actual.
        gemini_dict (Dict): Inventario actual de documentos en Gemini (para comparación de deltas).
        semaphore (asyncio.Semaphore): Semáforo para limitar la carga paralela.
        
    Returns:
        str: Resultado de la operación (UPLOADED, REPLACED, SKIPPED, ERROR).
    """
    async with semaphore:
        action = None
        # Lógica de detección de deltas
        if file_name not in gemini_dict:
            action = "UPLOADED"
        elif gcs_size != gemini_dict[file_name]["size"]:
            # Si el tamaño difiere, se considera un cambio de contenido y se reemplaza el documento
            try:
                gemini_client.delete_document(gemini_dict[file_name]["id"])
                action = "REPLACED"
            except Exception as e:
                logging.error(f"Error al eliminar {file_name} para reemplazo: {str(e)}")
                return "ERROR"
        else:
            # Si el archivo ya existe y tiene el mismo tamaño, se omite para optimizar cuotas
            return "SKIPPED"

        try:
            # Transferencia de datos: GCS -> Memoria -> Gemini
            # Se utiliza asyncio.to_thread para no bloquear el event loop con operaciones I/O del SDK
            data = await asyncio.to_thread(gcs_client.download_blob_to_bytes, bucket_name, file_name)
            metadata = {
                "bucket_name": bucket_name,
                "original_filename": file_name,
                "exact_size_bytes": str(gcs_size),
                "upload_date": datetime.utcnow().isoformat()
            }
            await asyncio.to_thread(gemini_client.upload_document, store_id, file_name, data, metadata)
            
            # Registro de éxito en la base de datos de auditoría
            log_sync_action(transaction_id, bucket_name, store_id, file_name, action, gcs_size, user_id)
            return action
        except Exception as e:
            logging.error(f"Fallo al procesar el archivo {file_name}: {str(e)}")
            log_sync_action(transaction_id, bucket_name, store_id, file_name, "ERROR_SYNC", gcs_size, user_id)
            return "ERROR"

async def sync_bucket_to_gemini(bucket_name: str, user_id: str, transaction_id: str, prefix: str = None, store_name: str = None) -> Dict:
    """
    Orquesta la sincronización masiva y concurrente entre GCS y Gemini File Search.
    Implementa un patrón de 'Mirroring' que incluye subidas, actualizaciones y limpieza de huérfanos.
    
    Args:
        bucket_name (str): Bucket de GCS a sincronizar.
        user_id (str): Usuario que solicita la sincronización.
        transaction_id (str): ID único de seguimiento.
        prefix (str, optional): Subdirectorio opcional dentro del bucket.
        store_name (str, optional): Nombre del repositorio en Gemini (por defecto el nombre del bucket).
        
    Returns:
        Dict: Resumen de la operación (conteo de subidas, omisiones, eliminaciones y errores).
    """
    summary = {"uploaded": 0, "skipped": 0, "deleted": 0, "errors": 0}
    store_display_name = store_name or bucket_name
    
    try:
        # 1. Resolución del Repositorio Destino
        all_stores = gemini_client.list_stores()
        target_store = next((s for s in all_stores if s["display_name"] == store_display_name), None)
        
        if not target_store:
            store_id = gemini_client.create_store(display_name=store_display_name)
            logging.info(f"Nuevo repositorio Gemini creado: {store_id} para {store_display_name}")
        else:
            store_id = target_store["id"]
        
        # 2. Análisis de Inventario Local (GCS)
        gcs_inventory = gcs_client.list_blobs_with_metadata(bucket_name, prefix=prefix)
        gcs_dict = {item["name"]: item["size"] for item in gcs_inventory}
        
        # 3. Análisis de Inventario Remoto (Gemini)
        gemini_items = gemini_client.list_documents(store_id)
        gemini_dict = {}
        for item in gemini_items:
            # Extracción de metadatos custom para validación de integridad
            meta = getattr(item, 'metadata', {})
            size_str = meta.get("exact_size_bytes", "-1")
            gemini_dict[item["display_name"]] = {
                "id": item["name"] if hasattr(item, 'name') else item.get("id"),
                "size": int(size_str)
            }
        
        # 4. Procesamiento Paralelo de Archivos (Limitado por Semáforo)
        # Se define un límite de concurrencia de 10 para evitar saturar el ancho de banda y cuotas de API
        semaphore = asyncio.Semaphore(10)
        tasks = []
        for file_name, gcs_size in gcs_dict.items():
            if file_name.endswith('/'): # Omitir directorios virtuales
                continue
            tasks.append(process_file_sync(
                file_name, gcs_size, bucket_name, store_id, user_id, transaction_id, gemini_dict, semaphore
            ))
        
        # Ejecución masiva y recolección de resultados
        results = await asyncio.gather(*tasks)
        for res in results:
            if res in ["UPLOADED", "REPLACED"]:
                summary["uploaded"] += 1
            elif res == "SKIPPED":
                summary["skipped"] += 1
            elif res == "ERROR":
                summary["errors"] += 1
                
        # 5. Fase de Limpieza de Huérfanos
        # Documentos que existen en Gemini pero ya no están presentes en el origen GCS
        for gemini_name, info in gemini_dict.items():
            if gemini_name not in gcs_dict:
                try:
                    gemini_client.delete_document(info["id"])
                    summary["deleted"] += 1
                    log_sync_action(transaction_id, bucket_name, store_id, gemini_name, "DELETED_ORPHAN", info["size"], user_id)
                    logging.info(f"Documento huérfano eliminado: {gemini_name}")
                except Exception as e:
                    logging.error(f"Error al eliminar documento huérfano {gemini_name}: {str(e)}")
                    summary["errors"] += 1
                    
        return summary

    except Exception as e:
        logging.error(f"Error crítico durante la sincronización del bucket {bucket_name}: {str(e)}")
        raise e