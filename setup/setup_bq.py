import os
import sys

# Add apis paths
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "apis", "stores"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "apis", "locations"))

from google.cloud import bigquery
from google.cloud.bigquery import SchemaField, Table, TimePartitioning, TimePartitioningType

from schemas.users import users_table_schema, users_table_config, authentication_log_schema, authentication_log_config
from schemas.stores import stores_table_schema, stores_table_config, stores_log_schema, stores_log_config
from schemas.locations import locations_table_schema, locations_table_config, locations_log_schema, locations_log_config

import subprocess
from google.oauth2.credentials import Credentials

project_id = "que-vino-23032025"

try:
    token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode("utf-8").strip()
    creds = Credentials(token)
    client = bigquery.Client(project=project_id, credentials=creds)
except Exception as e:
    print(f"Fallback to default ADC: {e}")
    client = bigquery.Client(project=project_id)

configs = [
    (users_table_config, users_table_schema),
    (authentication_log_config, authentication_log_schema),
    (stores_table_config, stores_table_schema),
    (stores_log_config, stores_log_schema),
    (locations_table_config, locations_table_schema),
    (locations_log_config, locations_log_schema),
]

def map_schema(schema_def):
    fields = []
    for field in schema_def:
        fields.append(SchemaField(
            name=field["name"],
            field_type=field["type"],
            mode=field.get("mode", "NULLABLE"),
            description=field.get("description", "")
        ))
    return fields

# Create tables
for config, schema in configs:
    table_id = config["table_id"]
    full_table_id = f"{project_id}.{table_id}"
    
    bq_schema = map_schema(schema)
    table = Table(full_table_id, schema=bq_schema)
    
    # Configure partitioning
    if "partitioning" in config:
        table.time_partitioning = TimePartitioning(
            type_=TimePartitioningType.DAY,
            field=config["partitioning"]
        )
    
    # Configure clustering
    if "clustering" in config:
        table.clustering_fields = config["clustering"]
        
    try:
        table = client.create_table(table, exists_ok=True)
        print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")
    except Exception as e:
        print(f"Error creating {full_table_id}: {e}")


