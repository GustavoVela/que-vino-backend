"""
setup_bq.py — Que Vino! BigQuery Setup Script
===============================================
Script centralizado para crear/actualizar todas las tablas de BigQuery del proyecto.
Ejecutar desde la raíz del repositorio:

    python setup/setup_bq.py

Tablas creadas:
  Dataset src_database:
    - users
    - stores
    - locations

  Dataset src_api_transactions:
    - authentication_log         (auth events)
    - stores_log                 (stores API audit)
    - locations_log              (locations API audit)
    - audio_api_log              (audio API request/response)
    - audio_generation_log       (audio generation business audit)
    - knowledge_store_api_log    (knowledge stores API audit)
    - knowledge_sync_log         (knowledge sync operations audit)

Constitución: Sección 2.3 — BigQuery como capa de datos y auditoría.
"""

import os
import sys
import subprocess

# ---------------------------------------------------------------------------
# Path setup — permite importar schemas desde cualquier API del proyecto
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(ROOT_DIR, "apis", "stores"))
sys.path.append(os.path.join(ROOT_DIR, "apis", "locations"))

from google.cloud import bigquery
from google.cloud.bigquery import SchemaField, Table, TimePartitioning, TimePartitioningType
from google.oauth2.credentials import Credentials

# ---------------------------------------------------------------------------
# Schemas de APIs existentes (stores, locations)
# ---------------------------------------------------------------------------
from schemas.users import (
    users_table_schema, users_table_config,
    authentication_log_schema, authentication_log_config,
)
from schemas.stores import (
    stores_table_schema, stores_table_config,
    stores_log_schema, stores_log_config,
)
from schemas.locations import (
    locations_table_schema, locations_table_config,
    locations_log_schema, locations_log_config,
)

# ---------------------------------------------------------------------------
# Configuración del proyecto
# ---------------------------------------------------------------------------
PROJECT_ID = "que-vino-23032025"
DATASET_DB = "src_database"
DATASET_TX = "src_api_transactions"

# ---------------------------------------------------------------------------
# Cliente BigQuery (intenta con token de gcloud, fallback a ADC)
# ---------------------------------------------------------------------------
try:
    token = subprocess.check_output(
        ["gcloud", "auth", "print-access-token"]
    ).decode("utf-8").strip()
    creds = Credentials(token)
    client = bigquery.Client(project=PROJECT_ID, credentials=creds)
    print("✅ Autenticado via gcloud token")
except Exception as e:
    print(f"⚠️  Fallback a ADC: {e}")
    client = bigquery.Client(project=PROJECT_ID)

# ---------------------------------------------------------------------------
# Definición inline de tablas de Audio API
# (schemas viven en apis/audio/schemas/bq_models.py como Pydantic models)
# ---------------------------------------------------------------------------
audio_api_log_schema = [
    {"name": "transaction_id",        "type": "STRING",    "mode": "REQUIRED",  "description": "UUID de la transacción"},
    {"name": "performed_by_user_id",  "type": "STRING",    "mode": "NULLABLE",  "description": "Firebase UID del usuario"},
    {"name": "transaction_api_type",  "type": "STRING",    "mode": "REQUIRED",  "description": "Método HTTP (GET, POST)"},
    {"name": "transaction_api_path",  "type": "STRING",    "mode": "REQUIRED",  "description": "Path del endpoint llamado"},
    {"name": "transaction_parameters","type": "STRING",    "mode": "NULLABLE",  "description": "Query params (JSON string)"},
    {"name": "payload_request",       "type": "STRING",    "mode": "NULLABLE",  "description": "Body de request (JSON string)"},
    {"name": "payload_response",      "type": "STRING",    "mode": "NULLABLE",  "description": "Body de response (JSON string)"},
    {"name": "event_timestamp",       "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp del evento"},
    {"name": "ingestion_timestamp",   "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp de inserción en BQ"},
]
audio_api_log_config = {
    "table_id": f"{DATASET_TX}.audio_api_log",
    "partitioning": "event_timestamp",
    "clustering": ["performed_by_user_id", "transaction_api_type"],
}

audio_generation_log_schema = [
    {"name": "generation_id",         "type": "STRING",    "mode": "REQUIRED",  "description": "UUID de generación"},
    {"name": "api_transaction_id",    "type": "STRING",    "mode": "REQUIRED",  "description": "Referencia al api_log"},
    {"name": "performed_by_user_id",  "type": "STRING",    "mode": "REQUIRED",  "description": "Firebase UID del usuario"},
    {"name": "provider",              "type": "STRING",    "mode": "REQUIRED",  "description": "ELEVENLABS | GOOGLE"},
    {"name": "voice_id",              "type": "STRING",    "mode": "REQUIRED",  "description": "ID de la voz usada"},
    {"name": "is_enriched",           "type": "BOOLEAN",   "mode": "REQUIRED",  "description": "¿Se enriqueció el texto con IA?"},
    {"name": "text_input",            "type": "STRING",    "mode": "REQUIRED",  "description": "Texto original enviado"},
    {"name": "text_processed",        "type": "STRING",    "mode": "NULLABLE",  "description": "Texto enriquecido (si aplica)"},
    {"name": "status",                "type": "STRING",    "mode": "REQUIRED",  "description": "SUCCESS | ERROR_*"},
    {"name": "event_timestamp",       "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp del evento"},
    {"name": "ingestion_timestamp",   "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp de inserción en BQ"},
]
audio_generation_log_config = {
    "table_id": f"{DATASET_TX}.audio_generation_log",
    "partitioning": "event_timestamp",
    "clustering": ["performed_by_user_id", "provider", "status"],
}

# ---------------------------------------------------------------------------
# Definición inline de tablas de Knowledge Stores API
# (schemas viven en apis/knowledge_stores/schemas/bq_schemas.py)
# ---------------------------------------------------------------------------
knowledge_api_log_schema = [
    {"name": "transaction_id",         "type": "STRING",    "mode": "REQUIRED",  "description": "UUID de la transacción"},
    {"name": "bucket_name",            "type": "STRING",    "mode": "REQUIRED",  "description": "Bucket GCS origen"},
    {"name": "store_id_gemini",        "type": "STRING",    "mode": "NULLABLE",  "description": "ID del FileSearchStore en Gemini"},
    {"name": "performed_by_user_id",   "type": "STRING",    "mode": "REQUIRED",  "description": "Firebase UID del usuario"},
    {"name": "transaction_api_type",   "type": "STRING",    "mode": "REQUIRED",  "description": "Tipo de operación (LIST_STORES, SYNC, DELETE_STORE, etc.)"},
    {"name": "transaction_db_type",    "type": "STRING",    "mode": "REQUIRED",  "description": "Método HTTP (GET, POST, DELETE)"},
    {"name": "event_timestamp",        "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp del evento"},
    {"name": "ingestion_timestamp",    "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp de inserción en BQ"},
]
knowledge_api_log_config = {
    "table_id": f"{DATASET_TX}.knowledge_store_api_log",
    "partitioning": "event_timestamp",
    "clustering": ["performed_by_user_id", "store_id_gemini", "transaction_api_type"],
}

knowledge_sync_log_schema = [
    {"name": "transaction_id",         "type": "STRING",    "mode": "REQUIRED",  "description": "UUID de la transacción de sync"},
    {"name": "bucket_name",            "type": "STRING",    "mode": "REQUIRED",  "description": "Bucket GCS origen"},
    {"name": "store_id_gemini",        "type": "STRING",    "mode": "REQUIRED",  "description": "ID del FileSearchStore en Gemini"},
    {"name": "file_name",              "type": "STRING",    "mode": "REQUIRED",  "description": "Ruta del archivo procesado"},
    {"name": "action_taken",           "type": "STRING",    "mode": "REQUIRED",  "description": "UPLOADED | SKIPPED | DELETED | ERROR"},
    {"name": "file_size_bytes",        "type": "INT64",     "mode": "NULLABLE",  "description": "Tamaño del archivo en bytes"},
    {"name": "performed_by_user_id",   "type": "STRING",    "mode": "REQUIRED",  "description": "Firebase UID del usuario"},
    {"name": "event_timestamp",        "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp del evento"},
    {"name": "ingestion_timestamp",    "type": "TIMESTAMP", "mode": "REQUIRED",  "description": "Timestamp de inserción en BQ"},
]
knowledge_sync_log_config = {
    "table_id": f"{DATASET_TX}.knowledge_sync_log",
    "partitioning": "event_timestamp",
    "clustering": ["performed_by_user_id", "store_id_gemini", "action_taken"],
}

# ---------------------------------------------------------------------------
# Mapa completo de tablas a crear
# (config, schema) — config["table_id"] = "dataset.table_name"
# ---------------------------------------------------------------------------
ALL_TABLES = [
    # ── src_database ──────────────────────────────────────────────────────
    (users_table_config,       users_table_schema),
    (stores_table_config,      stores_table_schema),
    (locations_table_config,   locations_table_schema),

    # ── src_api_transactions ───────────────────────────────────────────────
    (authentication_log_config,    authentication_log_schema),
    (stores_log_config,            stores_log_schema),
    (locations_log_config,         locations_log_schema),
    (audio_api_log_config,         audio_api_log_schema),
    (audio_generation_log_config,  audio_generation_log_schema),
    (knowledge_api_log_config,     knowledge_api_log_schema),
    (knowledge_sync_log_config,    knowledge_sync_log_schema),
]

# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def map_schema(schema_def: list) -> list[SchemaField]:
    """Convierte lista de dicts a objetos SchemaField de BigQuery."""
    return [
        SchemaField(
            name=field["name"],
            field_type=field["type"],
            mode=field.get("mode", "NULLABLE"),
            description=field.get("description", ""),
        )
        for field in schema_def
    ]


def ensure_dataset(dataset_id: str):
    """Crea el dataset si no existe."""
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{dataset_id}")
    dataset_ref.location = "US"
    try:
        client.create_dataset(dataset_ref, exists_ok=True)
        print(f"  📦 Dataset listo: {dataset_id}")
    except Exception as e:
        print(f"  ⚠️  No se pudo crear/verificar dataset {dataset_id}: {e}")


# ---------------------------------------------------------------------------
# Ejecución principal
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print()
    print("=" * 60)
    print("  Que Vino! — BigQuery Setup")
    print(f"  Proyecto: {PROJECT_ID}")
    print("=" * 60)

    # Asegurar datasets
    print("\n🗂️  Verificando datasets...")
    ensure_dataset(DATASET_DB)
    ensure_dataset(DATASET_TX)

    # Crear tablas
    print(f"\n📋 Creando {len(ALL_TABLES)} tablas...\n")
    created = 0
    errors = 0

    for config, schema in ALL_TABLES:
        table_id = config["table_id"]
        full_table_id = f"{PROJECT_ID}.{table_id}"

        bq_schema = map_schema(schema)
        table = Table(full_table_id, schema=bq_schema)

        if "partitioning" in config:
            table.time_partitioning = TimePartitioning(
                type_=TimePartitioningType.DAY,
                field=config["partitioning"],
            )

        if "clustering" in config:
            table.clustering_fields = config["clustering"]

        try:
            client.create_table(table, exists_ok=True)
            print(f"  ✅ {full_table_id}")
            created += 1
        except Exception as e:
            print(f"  ❌ {full_table_id}: {e}")
            errors += 1

    print()
    print("=" * 60)
    print(f"  ✅ {created} tablas OK  |  ❌ {errors} errores")
    print("=" * 60)
    print()
