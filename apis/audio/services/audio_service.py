import asyncio
import uuid
from typing import List, Dict, Any, Tuple, Optional
from cachetools import TTLCache

from config import settings
from services.providers.google_tts import GoogleTTSProvider
from services.providers.elevenlabs import ElevenLabsProvider
from services.gemini_service import gemini_service
from services.gcs_service import gcs_service
from core.db import bq_service
from schemas.bq_models import AudioGenerationLog




class AudioService:
    def __init__(self):
        # Initialize providers
        self.google = GoogleTTSProvider(settings.project_id)
        self.elevenlabs = ElevenLabsProvider(settings.ELEVENLABS_AUDIO_API_KEY)
        self.providers = {
            "GOOGLE": self.google,
            "ELEVENLABS": self.elevenlabs
        }
        
        # 24h cache (86400 seconds)
        self.voice_cache = TTLCache(maxsize=1, ttl=86400)
        self.model_cache = TTLCache(maxsize=1, ttl=86400)

    async def get_all_voices(self) -> List[Dict[str, Any]]:
        """Combine all voices from providers with 24h cache. Resilient to partial failures."""
        if "voices" in self.voice_cache:
            return self.voice_cache["voices"]
        
        # Run in parallel with return_exceptions=True
        tasks = [p.list_voices() for p in self.providers.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter successes and flatten
        flat_list = []
        for res in results:
            if isinstance(res, list):
                flat_list.extend(res)
            else:
                # Log error or handle partial failure gracefully
                print(f"Partial failure in list_voices: {str(res)}")
        
        self.voice_cache["voices"] = flat_list
        return flat_list

    async def get_all_models(self) -> List[Dict[str, Any]]:
        """Combine all models from providers with 24h cache. Resilient to partial failures."""
        if "models" in self.model_cache:
            return self.model_cache["models"]
        
        # Run in parallel with return_exceptions=True
        tasks = [p.list_models() for p in self.providers.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter successes and flatten
        flat_list = []
        for res in results:
            if isinstance(res, list):
                flat_list.extend(res)
            else:
                # Log error or handle partial failure gracefully
                print(f"Partial failure in list_models: {str(res)}")
        
        self.model_cache["models"] = flat_list
        return flat_list

    async def generate_audio(
        self,
        text: str,
        provider_key: str,
        voice_id: str,
        output_format: str,
        enrich_audio: bool = False,
        **kwargs
    ) -> Tuple[bytes, Dict[str, Any]]:
        """
        Main orchestration flow:
        1. Enrich text with Gemini (if requested)
        2. Synthesize audio with provider
        3. Return binary + metadata for audit
        """
        provider = self.providers.get(provider_key.upper())
        if not provider:
            raise ValueError(f"Provider {provider_key} not supported.")

        generation_id = str(uuid.uuid4())
        text_processed = None
        enrichment_status = "SKIPPED"
        is_enriched_success = False

        # 1. Enrichment with IA
        if enrich_audio:
            text_processed, is_enriched_success = await gemini_service.enrich_text(
                text, 
                provider_key.upper()
            )
            enrichment_status = "SUCCESS" if is_enriched_success else "FAILED"
        
        # 2. Synthesis
        # Use enriched text if success, else original
        synthesis_text = text_processed if is_enriched_success else text
        
        audio_bytes = await provider.synthesize(
            text=synthesis_text,
            voice_id=voice_id,
            output_format=output_format,
            **kwargs
        )

        # 3. Audit Metadata
        metadata = {
            "generation_id": generation_id,
            "enrichment_status": enrichment_status,
            "is_enriched": is_enriched_success,
            "text_processed": text_processed,
            "original_text": text
        }

        return audio_bytes, metadata

    async def persist_audit_async(
        self, 
        audio_bytes: bytes, 
        metadata: Dict[str, Any], 
        provider_key: str, 
        voice_id: str, 
        user_id: str,
        transaction_id: str
    ):
        """Standard coordination of GCS and BQ async audit."""
        # GCS
        gcs_metadata = {
            "user_id": user_id,
            "provider": provider_key,
            "voice_id": voice_id
        }
        gcs_service.upload_audio_bytes(
            audio_bytes, 
            metadata["generation_id"], 
            "mp3", 
            gcs_metadata
        )

        # BQ
        gen_log = AudioGenerationLog(
            generation_id=metadata["generation_id"],
            api_transaction_id=transaction_id,
            performed_by_user_id=user_id,
            provider=provider_key,
            voice_id=voice_id,
            is_enriched=metadata["is_enriched"],
            text_input=metadata["original_text"],
            text_processed=metadata["text_processed"],
            status="SUCCESS" if metadata["enrichment_status"] != "FAILED" else "SUCCESS_WITHOUT_ENRICHMENT"
        )
        bq_service.log_audio_generation(gen_log)


audio_service = AudioService()
