from google.cloud import bigquery

def get_users_schema():
    return [
        bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("email", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("email_verified", "BOOL", mode="REQUIRED"),
        bigquery.SchemaField("display_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("photo_url", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("phone_number", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("provider_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("created_at", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("updated_at", "TIMESTAMP", mode="REQUIRED"),
    ]

def get_auth_log_schema():
    return [
        bigquery.SchemaField("transaction_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("user_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("email", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("status", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("error_message", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("event_timestamp", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("ingestion_timestamp", "TIMESTAMP", mode="REQUIRED"),
    ]

def get_store_api_log_schema():
    return [
        bigquery.SchemaField("transaction_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("bucket_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("store_id_gemini", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("performed_by_user_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("transaction_api_type", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("transaction_db_type", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("event_timestamp", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("ingestion_timestamp", "TIMESTAMP", mode="REQUIRED"),
    ]

def get_sync_log_schema():
    return [
        bigquery.SchemaField("transaction_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("bucket_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("store_id_gemini", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("file_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("action_taken", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("file_size_bytes", "INT64", mode="NULLABLE"),
        bigquery.SchemaField("performed_by_user_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("event_timestamp", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("ingestion_timestamp", "TIMESTAMP", mode="REQUIRED"),
    ]
