stores_table_schema = [
    {"name": "id", "type": "STRING", "mode": "REQUIRED", "description": "Generado como UUID4 por backend."},
    {"name": "name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre de la Tienda"},
    {"name": "type", "type": "STRING", "mode": "NULLABLE", "description": "Digital, Mixta, Fisica"},
    {"name": "digital_platform", "type": "STRING", "mode": "NULLABLE", "description": "Plataforma (ej. Shopify)"},
    {"name": "is_producer", "type": "BOOL", "mode": "REQUIRED", "description": "¿Productor?"},
    {"name": "has_wine_club", "type": "BOOL", "mode": "REQUIRED", "description": "¿Tiene club de vino?"},
    {"name": "representative_name", "type": "STRING", "mode": "NULLABLE", "description": "Representante"},
    {"name": "country_code", "type": "STRING", "mode": "REQUIRED", "description": "Codigo Pais"},
    {"name": "country_name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre Pais"},
    {"name": "state_code", "type": "STRING", "mode": "NULLABLE", "description": "Codigo Estado"},
    {"name": "state_name", "type": "STRING", "mode": "NULLABLE", "description": "Nombre Estado"},
    {"name": "city_code", "type": "STRING", "mode": "REQUIRED", "description": "Codigo Ciudad"},
    {"name": "city_name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre Ciudad"},
    {"name": "address", "type": "STRING", "mode": "NULLABLE", "description": "Domicilio"},
    {"name": "contact_email", "type": "STRING", "mode": "NULLABLE", "description": "Correo electronico"},
    {"name": "contact_phone", "type": "STRING", "mode": "NULLABLE", "description": "Telefono"},
    {"name": "website_url", "type": "STRING", "mode": "NULLABLE", "description": "URL de sitio web"},
    {"name": "social_media", "type": "JSON", "mode": "NULLABLE", "description": "Redes sociales"},
    {"name": "description", "type": "STRING", "mode": "NULLABLE", "description": "Descripcion Larga"},
    {"name": "created_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Creacion"},
    {"name": "updated_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Actualizacion"}
]

stores_table_config = {
    "table_id": "src_database.stores",
    "partitioning": "created_at",
    "clustering": ["type", "country_code", "state_code", "city_code"]
}

stores_log_schema = [
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

stores_log_config = {
    "table_id": "src_api_transactions.stores_log",
    "partitioning": "event_timestamp",
    "clustering": ["transaction_api_type", "transaction_api_path", "transaction_db_type", "performed_by_user_id"]
}
