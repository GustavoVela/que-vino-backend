from typing import Dict, Any, List

users_table_schema = [
    {"name": "id", "type": "STRING", "mode": "REQUIRED", "description": "UID de Firebase (Primary Key)."},
    {"name": "email", "type": "STRING", "mode": "REQUIRED", "description": "Correo electronico principal del usuario."},
    {"name": "email_verified", "type": "BOOL", "mode": "REQUIRED", "description": "Indica si el correo ha sido verificado en el proveedor."},
    {"name": "display_name", "type": "STRING", "mode": "REQUIRED", "description": "Nombre a mostrar del usuario."},
    {"name": "photo_url", "type": "STRING", "mode": "NULLABLE", "description": "URL de la foto de perfil."},
    {"name": "phone_number", "type": "STRING", "mode": "NULLABLE", "description": "Numero de telefono asociado a la cuenta."},
    {"name": "provider_id", "type": "STRING", "mode": "NULLABLE", "description": "Proveedor de identidad."},
    {"name": "created_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Momento de creacion en nuestra base de datos."},
    {"name": "updated_at", "type": "TIMESTAMP", "mode": "REQUIRED", "description": "Ultima vez que el usuario inicio sesion o actualizo su token."}
]

users_table_config = {
    "table_id": "src_database.users",
    "partitioning": "created_at",
    "clustering": ["provider_id", "email_verified"]
}

authentication_log_schema = [
    {"name": "transaction_id", "type": "STRING", "mode": "REQUIRED"},
    {"name": "user_id", "type": "STRING", "mode": "NULLABLE"},
    {"name": "email", "type": "STRING", "mode": "REQUIRED"},
    {"name": "status", "type": "STRING", "mode": "REQUIRED"},
    {"name": "error_message", "type": "STRING", "mode": "NULLABLE"},
    {"name": "event_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
    {"name": "ingestion_timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"}
]

authentication_log_config = {
    "table_id": "src_api_transactions.authentication_log",
    "partitioning": "event_timestamp",
    "clustering": ["status", "email", "user_id"]
}
