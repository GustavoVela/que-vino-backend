import pytest
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from services.audio_service import AudioService
from schemas.bq_models import AudioGenerationLog

@pytest.fixture
def audio_service():
    # Patch the providers to avoid API calls
    with patch('services.providers.google_tts.GoogleTTSProvider'), \
         patch('services.providers.elevenlabs.ElevenLabsProvider'):
        return AudioService()

@pytest.mark.asyncio
async def test_generate_audio_success(audio_service):
    """Verifica el flujo completo de generación con enriquecimiento exitoso."""
    # Mock de Gemini
    with patch('services.audio_service.gemini_service.enrich_text', new_callable=AsyncMock) as mock_gemini:
        mock_gemini.return_value = ("Texto Enriquecido", True)
        
        # Mock del proveedor ( ElevenLabs en este caso )
        audio_service.elevenlabs.synthesize = AsyncMock(return_value=b"fake_audio_bytes")
        
        audio_bytes, metadata = await audio_service.generate_audio(
            text="Texto Original",
            provider_key="ELEVENLABS",
            voice_id="rachel",
            output_format="mp3",
            enrich_audio=True
        )
        
        assert audio_bytes == b"fake_audio_bytes"
        assert metadata["is_enriched"] is True
        assert metadata["text_processed"] == "Texto Enriquecido"
        assert metadata["enrichment_status"] == "SUCCESS"

@pytest.mark.asyncio
async def test_persist_audit_sync(audio_service):
    """Verifica la orquestación asíncrona de auditoría (GCS + BQ)."""
    mock_audio = b"dummy_audio"
    mock_metadata = {
        "generation_id": "tx-123",
        "is_enriched": True,
        "original_text": "hello",
        "text_processed": "enriched hello",
        "enrichment_status": "SUCCESS"
    }

    with patch('services.audio_service.gcs_service.upload_audio_bytes') as mock_gcs, \
         patch('services.audio_service.bq_service.log_audio_generation') as mock_bq:
        
        await audio_service.persist_audit_async(
            audio_bytes=mock_audio,
            metadata=mock_metadata,
            provider_key="ELEVENLABS",
            voice_id="rachel",
            user_id="user-456",
            transaction_id="tx-999"
        )
        
        # Verificar subida a GCS
        mock_gcs.assert_called_once()
        args, _ = mock_gcs.call_args
        assert args[1] == "tx-123" # generation_id
        
        # Verificar log en BQ
        mock_bq.assert_called_once()
        gen_log = mock_bq.call_args[0][0]
        assert isinstance(gen_log, AudioGenerationLog)
        assert gen_log.generation_id == "tx-123"
        assert gen_log.status == "SUCCESS"

def test_upsert_user_bq_audit():
    """Verifica que la función de upsert genere la consulta SQL correcta."""
    from core.auth_middleware import upsert_user_bq
    
    decoded_token = {
        "uid": "123",
        "email": "test@quevino.mx",
        "name": "Test User",
        "picture": "http://pic.com",
        "firebase": {"sign_in_provider": "google.com"}
    }
    
    with patch('core.auth_middleware.bq_service.execute_query') as mock_exec:
        upsert_user_bq(decoded_token)
        mock_exec.assert_called_once()
        query = mock_exec.call_args[0][0]
        assert "MERGE" in query
        assert "src_database.users" in query
