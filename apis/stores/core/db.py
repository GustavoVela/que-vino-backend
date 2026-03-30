from google.cloud import bigquery
from fastapi import HTTPException
from config import settings
import logging

_client = None
BQ_TIMEOUT = 5.0

def get_bq_client() -> bigquery.Client:
    """Devuelve el cliente de BigQuery instanciado."""
    global _client
    if _client is None:
        _client = bigquery.Client(project=settings.project_id)
    return _client

def execute_query(query: str, parameters: list = None) -> bigquery.table.RowIterator:
    """
    Ejecuta una consulta en BigQuery imponiendo un timeout duro de 5 segundos.
    Lanza HTTPException con estatus 500 en caso de agotarse el tiempo.
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
