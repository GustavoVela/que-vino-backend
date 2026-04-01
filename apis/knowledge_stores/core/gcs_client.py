from google.cloud import storage
import logging
from typing import List, Dict
from config import settings

_storage_client = None

import subprocess
from google.oauth2 import credentials as oauth2_credentials

def get_gcs_client() -> storage.Client:
    """Devuelve el cliente de GCS con fallback para entorno local."""
    global _storage_client
    if _storage_client is None:
        try:
            # Intentar usar ADC (Cloud Run standard)
            _storage_client = storage.Client(project=settings.project_id)
        except Exception:
            # Fallback local usando el token activo de gcloud
            try:
                logging.info("ADC not found; attempting local gcloud token fallback.")
                token = subprocess.check_output(
                    ['gcloud', 'auth', 'print-access-token'], 
                    stderr=subprocess.DEVNULL
                ).decode('utf-8').strip()
                creds = oauth2_credentials.Credentials(token)
                _storage_client = storage.Client(project=settings.project_id, credentials=creds)
            except Exception as inner_e:
                logging.error(f"Failed to initialize GCS client: {str(inner_e)}")
                raise inner_e
                
    return _storage_client

def list_blobs_with_metadata(bucket_name: str, prefix: str = None) -> List[Dict]:
    """
    Lista todos los archivos de un bucket (opcionalmente bajo un prefijo) con su tamaño.
    Retorna una lista de dicts: {'name': str, 'size': int}
    """
    try:
        client = get_gcs_client()
        blobs = client.list_blobs(bucket_name, prefix=prefix)
        
        inventory = []
        for blob in blobs:
            inventory.append({
                "name": blob.name,
                "size": blob.size
            })
        return inventory
    except Exception as e:
        logging.error(f"Error listing GCS blobs in {bucket_name}: {str(e)}")
        raise e

def download_blob_to_bytes(bucket_name: str, blob_name: str) -> bytes:
    """Descarga el contenido de un blob a memoria."""
    try:
        client = get_gcs_client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        return blob.download_as_bytes()
    except Exception as e:
        logging.error(f"Error downloading blob {blob_name} from {bucket_name}: {str(e)}")
        raise e
