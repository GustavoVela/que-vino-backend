from typing import Dict, Any, List

locations_table_schema = [
    {"name": "id", "type": "STRING", "mode": "REQUIRED", "description": "Generado como UUID4"},
    {"name": "country_code", "type": "STRING", "mode": "REQUIRED", "description": "Codigo Pais Iso"},
    {"name": "country_name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre Pais"},
    {"name": "state_code", "type": "STRING", "mode": "NULLABLE", "description": "Codigo Estado"},
    {"name": "state_name", "type": "STRING", "mode": "NULLABLE", "description": "Nombre Estado"},
    {"name": "city_code", "type": "STRING", "mode": "REQUIRED", "description": "Codigo Ciudad"},
    {"name": "city_name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre Ciudad"},
    {"name": "latitude", "type": "FLOAT", "mode": "NULLABLE", "description": "Coordenadas latitud"},
    {"name": "longitude", "type": "FLOAT", "mode": "NULLABLE", "description": "Coordenadas longitud"},
    {"name": "created_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Momento de creacion."},
    {"name": "updated_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Actualizacion."}
]

locations_table_config = {
    "table_id": "src_database.locations",
    "partitioning": "created_at",
    "clustering": ["country_code", "state_code", "city_code"]
}

locations_log_schema = [
    {"name": "transaction_id", "type": "STRING", "mode": "REQUIRED"},
    {"name": "performed_by_user_id", "type": "STRING", "mode": "NULLABLE"},
    {"name": "performed_by_email", "type": "STRING", "mode": "NULLABLE"},
    {"name": "transaction_api_type", "type": "STRING", "mode": "REQUIRED"},
    {"name": "transaction_api_path", "type": "STRING", "mode": "REQUIRED"},
    {"name": "transaction_db_type", "type": "STRING", "mode": "REQUIRED"},
    {"name": "transaction_parameters", "type": "JSON", "mode": "NULLABLE"},
    {"name": "payload_before", "type": "JSON", "mode": "NULLABLE"},
    {"name": "payload_after", "type": "JSON", "mode": "NULLABLE"},
    {"name": "event_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
    {"name": "ingestion_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"}
]

locations_log_config = {
    "table_id": "src_api_transactions.locations_log",
    "partitioning": "event_timestamp",
    "clustering": ["transaction_api_type", "transaction_api_path", "transaction_db_type", "performed_by_user_id"]
}
