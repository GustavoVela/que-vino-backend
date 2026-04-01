from google import genai
from google.genai import types
from config import settings
import logging
from typing import Optional, List
import io

"""
Módulo de cliente para la integración con Gemini GenAI (SDK v1.70.0+).
Este módulo centraliza todas las operaciones de File Search Stores (RAG) 
utilizando el nuevo estándar Native (AI Studio) para el proyecto Que Vino!.
"""

# Configuración y validación del cliente Gemini GenAI
# El nuevo SDK google-genai unifica las capacidades de Vertex AI y AI Studio 
# en una interfaz agéntica coherente.
client_args = {}
if settings.effective_google_api_key:
    # Si se detecta una API Key en la configuración, se instancia en modo Native
    # Esto es ideal para desarrollo local y acceso directo a capacidades de búsqueda.
    client_args["api_key"] = settings.effective_google_api_key
    client_args["http_options"] = {'api_version': 'v1alpha'} # File Search opera en v1alpha en el stack de 2026
else:
    # Para despliegues en Cloud Run, se utiliza Application Default Credentials (ADC)
    # y la identidad de la Cuenta de Servicio asignada al microservicio.
    logging.info("Inicializando cliente Google Gen AI mediante ADC (Identidad de GCP)")
    client_args["vertexai"] = False 

# Cliente global persistente para eficiencia en el manejo de conexiones
client = genai.Client(**client_args)

def get_store_client():
    """
    Provee acceso a la instancia global pre-configurada del cliente de Gemini.
    
    Returns:
        genai.Client: Instancia configurada del cliente de Google GenAI.
    """
    return client

def list_stores() -> List[dict]:
    """
    Obtiene el listado completo de repositorios de búsqueda (File Search Stores).
    
    Returns:
        List[dict]: Colección de diccionarios con metadatos base ('id', 'display_name').
        
    Raises:
        Exception: Si existe un fallo en la comunicación con el plano de control de Gemini.
    """
    try:
        stores = client.file_search_stores.list()
        # El SDK retorna un iterador de objetos FileSearchStore con ID de recurso completo
        return [{"id": s.name, "display_name": s.display_name} for s in stores]
    except Exception as e:
        logging.error(f"Error al listar repositorios de Gemini: {str(e)}")
        raise e

def create_store(display_name: str) -> str:
    """
    Crea un nuevo repositorio lógico para indexación de documentos RAG.
    
    Args:
        display_name (str): Nombre amigable para identificar el repositorio.
        
    Returns:
        str: El ID de recurso único generado por Gemini (formato: fileSearchStores/{id}).
    """
    try:
        store = client.file_search_stores.create(
            config=types.CreateFileSearchStoreConfig(display_name=display_name)
        )
        return store.name
    except Exception as e:
        logging.error(f"Error al crear el repositorio '{display_name}': {str(e)}")
        raise e

def delete_store(store_name: str):
    """
    Elimina permanentemente un repositorio de búsqueda y todos sus documentos indexados.
    
    Args:
        store_name (str): ID de recurso completo del repositorio a eliminar.
    """
    try:
        client.file_search_stores.delete(name=store_name)
    except Exception as e:
        logging.error(f"Error al eliminar el repositorio Gemini {store_name}: {str(e)}")
        raise e

def list_documents(store_name: str) -> List[dict]:
    """
    Lista todos los documentos cargados en un repositorio específico.
    
    Args:
        store_name (str): ID de recurso completo del repositorio.
        
    Returns:
        List[dict]: Listado de documentos con su nombre de visualización y metadatos.
    """
    try:
        # En el SDK 1.x, el parent es el nombre completo del store
        docs = client.file_search_stores.documents.list(parent=store_name)
        return [
            {
                "id": d.name, 
                "display_name": d.display_name, 
                "metadata": getattr(d, 'metadata', {})
            } for d in docs
        ]
    except Exception as e:
        logging.error(f"Error al listar documentos en {store_name}: {str(e)}")
        raise e

def delete_document(doc_name: str):
    """
    Elimina un documento individual del índice de búsqueda.
    
    Args:
        doc_name (str): ID de recurso completo del documento.
    """
    try:
        client.file_search_stores.documents.delete(name=doc_name)
    except Exception as e:
        logging.error(f"Error al eliminar el documento {doc_name}: {str(e)}")
        raise e

def upload_document(store_name: str, display_name: str, data: bytes, metadata: dict):
    """
    Indexa un nuevo documento en el repositorio para habilitar capacidades de búsqueda RAG.
    Realiza una carga directa mediante un archivo temporal compatible con el SDK.
    
    Args:
        store_name (str): Repositorio destino del documento.
        display_name (str): Título visible del documento.
        data (bytes): Contenido binario del archivo.
        metadata (dict): Metadatos adicionales para filtrado semántico.
        
    Returns:
        str: ID del documento creado o identificador de operación pendiente.
    """
    try:
        import tempfile
        import os
        
        # El SDK de Gemini Native prefiere rutas de archivos reales para la carga inicial
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
            tmp.write(data)
            tmp_path = tmp.name
            
        try:
            # Operación de carga atómica e indexación
            doc = client.file_search_stores.upload_to_file_search_store(
                file=tmp_path,
                file_search_store_name=store_name,
                config=types.UploadToFileSearchStoreConfig(
                    display_name=display_name
                )
            )
            # Retorna el nombre del recurso si la operación fue inmediata (LRO)
            return doc.name if hasattr(doc, 'name') else "Operación_en_Progreso"
        finally:
            # Limpieza estricta de archivos temporales post-carga
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
                
    except Exception as e:
        logging.error(f"Error al subir el documento '{display_name}' a {store_name}: {str(e)}")
        raise e
