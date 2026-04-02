from google.cloud import storage
from config import settings
from core.logger import logger
from typing import Dict, Any

"""
Servicio de almacenamiento en GCS para auditoría de audio.
Utiliza el bucket específico de audio definido en la configuración (Sección 6.1).
"""

class GCSService:
    def __init__(self, bucket_name: str):
        self.client = storage.Client()
        self.bucket_name = bucket_name

    def upload_audio_bytes(
        self, 
        audio_bytes: bytes, 
        generation_id: str, 
        output_format: str,
        metadata: Dict[str, str] = None
    ) -> bool:
        """
        Sube bytes de audio al bucket de GCS (Bóveda de Auditoría).
        Ruta: /generations/{generation_id}.{output_format}
        """
        try:
            bucket = self.client.bucket(self.bucket_name)
            # Ruta estandarizada: /{service}/{type}/{id}.{ext} (Sección 2.6)
            filename = f"{settings.GCS_AUDIO_FOLDER}/generations/{generation_id}.{output_format}"
            blob = bucket.blob(filename)
            
            # Definición de Content-Type según el formato solicitado
            content_type = "audio/mpeg" if output_format == "mp3" else "audio/wav"
            blob.content_type = content_type
            
            # Inyección de metadatos de auditoría del usuario y proveedor
            if metadata:
                blob.metadata = metadata
            
            # Carga inmutable (Sección 2.1)
            blob.upload_from_string(
                audio_bytes,
                content_type=content_type
            )
            
            logger.info(f"Audio {generation_id} subido exitosamente a GCS: {filename}")
            return True
        except Exception as e:
            logger.error(f"Fallo al subir audio {generation_id} a GCS: {str(e)}")
            return False


# Instancia configurada con la variable de entorno específica para audio (Sección 1.1)
gcs_service = GCSService(settings.GCS_AUDIO_BUCKET_NAME)
