from google.cloud import bigquery
from fastapi import HTTPException
from config import settings
import logging
from datetime import datetime
import uuid

# Singleton client
_client = None
BQ_TIMEOUT = 5.0

def log_api_transaction_async(bucket_name: str, store_id: str, user_id: str, api_type: str, db_type: str = "READ"):
    """Log de transacciones de lectura/listado."""
    row = {
        "transaction_id": str(uuid.uuid4()),
        "bucket_name": bucket_name,
        "store_id_gemini": store_id,
        "performed_by_user_id": user_id,
        "transaction_api_type": api_type,
        "transaction_db_type": db_type,
        "event_timestamp": datetime.utcnow().isoformat() + "Z"
    }
    log_event_async(settings.bq_dataset_transactions, settings.table_store_api_log, row)

def get_bq_client() -> bigquery.Client:
    """Devuelve el cliente de BigQuery instanciado."""
    global _client
    if _client is None:
        _client = bigquery.Client(project=settings.project_id)
    return _client

def execute_query(query: str, parameters: list = None) -> bigquery.table.RowIterator:
    """
    Ejecuta una consulta en BigQuery imponiendo un timeout de 5 segundos.
    """
    processed_params = []
    if parameters:
        for p in parameters:
            if isinstance(p, dict):
                processed_params.append(bigquery.ScalarQueryParameter(p['name'], p['type'], p['value']))
            else:
                processed_params.append(p)

    job_config = bigquery.QueryJobConfig(
        query_parameters=processed_params
    )
    
    try:
        client = get_bq_client()
        query_job = client.query(query, job_config=job_config)
        return query_job.result(timeout=BQ_TIMEOUT)
    except Exception as e:
        logging.error(f"BigQuery Error/Timeout: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "error_code": "DATABASE_ERROR",
                "message": "Database query failed or timed out",
                "detail": str(e)
            }
        )

def log_event_async(dataset_name: str, table_name: str, row: dict):
    """
    Función para ser ejecutada en BackgroundTasks. 
    Inserta una fila en BigQuery de forma asíncrona respecto al request HTTP.
    """
    try:
        client = get_bq_client()
        table_id = f"{settings.project_id}.{dataset_name}.{table_name}"
        
        # Ensure ingestion_timestamp if not present
        if "ingestion_timestamp" not in row:
            row["ingestion_timestamp"] = datetime.utcnow().isoformat()
            
        errors = client.insert_rows_json(table_id, [row])
        if errors:
            logging.error(f"Async BQ Log Error in {table_id}: {errors}")
        else:
            logging.info(f"Async BQ Log Success in {table_id}")
    except Exception as e:
        logging.error(f"Critical Async BQ Log Failure: {str(e)}")
        # We don't raise exception here as it's a background task
