import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from google.cloud import bigquery
from config import settings
from core.logger import logger
from schemas.bq_models import APITransactionBase, AudioGenerationLog


class BigQueryService:
    def __init__(self, project_id: str, dataset_id: str):
        self.client = bigquery.Client(project=project_id)
        self.dataset_id = dataset_id

    def _prepare_json(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert datetime to string and ensure JSON serializable."""
        processed = {}
        for k, v in data.items():
            if isinstance(v, datetime):
                processed[k] = v.isoformat()
            elif isinstance(v, (dict, list)):
                processed[k] = json.dumps(v)
            else:
                processed[k] = v
        return processed

    def execute_query(self, query: str, parameters: Optional[List[Dict[str, Any]]] = None):
        """Execute a parameterized query in BigQuery."""
        try:
            job_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter(p["name"], p["type"], p["value"])
                    for p in (parameters or [])
                ]
            )
            query_job = self.client.query(query, job_config=job_config)
            return query_job.result()
        except Exception as e:
            logger.error(f"BQ query error: {str(e)}")
            raise e

    def log_api_transaction(self, log_entry: APITransactionBase):
        """Log API Request/Response to BigQuery."""
        try:
            table_ref = f"{settings.bq_dataset_transactions}.{settings.table_audio_api_log}"
            entry_dict = log_entry.model_dump()
            if not entry_dict.get("ingestion_timestamp"):
                entry_dict["ingestion_timestamp"] = datetime.utcnow()

            errors = self.client.insert_rows_json(
                table_ref,
                [self._prepare_json(entry_dict)]
            )
            if errors:
                logger.error(f"BQ errors logging transaction: {errors}")
        except Exception as e:
            logger.error(f"Failed to log API transaction: {str(e)}")

    def log_audio_generation(self, gen_log: AudioGenerationLog):
        """Log Business Audit details to BigQuery."""
        try:
            table_ref = f"{settings.bq_dataset_transactions}.{settings.table_audio_generation_log}"
            entry_dict = gen_log.model_dump()
            if not entry_dict.get("ingestion_timestamp"):
                entry_dict["ingestion_timestamp"] = datetime.utcnow()

            errors = self.client.insert_rows_json(
                table_ref,
                [self._prepare_json(entry_dict)]
            )
            if errors:
                logger.error(f"BQ errors logging generation: {errors}")
        except Exception as e:
            logger.error(f"Failed to log Audio generation: {str(e)}")

    def log_event_async(self, dataset: str, table: str, row: Dict[str, Any]):
        """General purpose row insertion for backgrounds."""
        try:
            table_ref = f"{dataset}.{table}"
            errors = self.client.insert_rows_json(table_ref, [self._prepare_json(row)])
            if errors:
                logger.error(f"BQ errors log_event_async: {errors}")
        except Exception as e:
            logger.error(f"Failed in log_event_async: {str(e)}")


# Singleton instance
bq_service = BigQueryService(settings.project_id, settings.bq_dataset_transactions)
