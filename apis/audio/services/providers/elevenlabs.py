import httpx
from typing import List, Dict, Any
from .base import TTSProvider


class ElevenLabsProvider(TTSProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "xi-api-key": self.api_key or "",
            "Content-Type": "application/json"
        }
        if not self.api_key:
            from core.logger import logger
            logger.warning("ElevenLabsProvider initialized without API Key. Calls will fail.")

    def provider_name(self) -> str:
        return "ELEVENLABS"

    async def list_voices(self) -> List[Dict[str, Any]]:
        """List and map ElevenLabs voices to standard format."""
        from core.logger import logger
        try:
            if not self.api_key:
                logger.error("ElevenLabs list_voices skipped: No API Key configured.")
                return []
                
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/voices", 
                    headers=self.headers,
                    timeout=30.0
                )
                if response.status_code != 200:
                    logger.error(f"ElevenLabs list_voices failed: {response.status_code} - {response.text}")
                    return []
                    
                data = response.json()
                
                standardized = []
                for voice in data.get("voices", []):
                    standardized.append({
                        "provider": self.provider_name(),
                        "voice_id": voice.get("voice_id"),
                        "name": voice.get("name"),
                        "category": voice.get("category"),
                        "labels": voice.get("labels", {}),
                        "description": voice.get("description"),
                        "preview_url": voice.get("preview_url")
                    })
                return standardized
        except Exception as e:
            logger.error(f"ElevenLabs list_voices unexpected exception: {str(e)}")
            return []

    async def list_models(self) -> List[Dict[str, Any]]:
        """List available ElevenLabs models."""
        from core.logger import logger
        try:
            if not self.api_key:
                return []
                
            async with httpx.AsyncClient() as client:
                # Cache-Control or similar can be added if needed
                response = await client.get(
                    f"{self.base_url}/models", 
                    headers=self.headers,
                    timeout=30.0
                )
                if response.status_code != 200:
                    logger.error(f"ElevenLabs list_models failed: {response.status_code} - {response.text}")
                    return []
                data = response.json()
                
                standardized = []
                for model in data:
                    standardized.append({
                        "provider": self.provider_name(),
                        "model_id": model.get("model_id"),
                        "name": model.get("name"),
                        "description": model.get("description"),
                        "can_do_text_to_speech": model.get("can_do_text_to_speech"),
                        "languages": model.get("languages", [])
                    })
                return standardized
        except Exception as e:
            logger.error(f"ElevenLabs list_models unexpected exception: {str(e)}")
            return []

    async def synthesize(self, text: str, voice_id: str, output_format: str, **kwargs) -> bytes:
        """Execute ElevenLabs TTS Synthesis."""
        from core.logger import logger
        try:
            if not self.api_key:
                raise ValueError("Cannot synthesize: ElevenLabs API Key is missing.")

            # Map standard formats to ElevenLabs specific IDs
            el_format = "mp3_44100_128" if output_format == "mp3" else "pcm_44100"
            
            # User model_id if passed, fallback to multilingual_v2
            # Use 'model_id' or 'model' key as requested by user
            model_id = kwargs.get("model_id") or kwargs.get("model") or "eleven_multilingual_v2"
            
            async with httpx.AsyncClient() as client:
                url = f"{self.base_url}/text-to-speech/{voice_id}"
                
                payload = {
                    "text": text,
                    "model_id": model_id
                }
                
                params = {"output_format": el_format}
                
                logger.info(f"ElevenLabs synthesis request: voice={voice_id}, model={model_id}, format={el_format}")
                
                response = await client.post(
                    url, 
                    json=payload, 
                    headers=self.headers, 
                    params=params,
                    timeout=90.0 # Audio generation is slow
                )
                
                if response.status_code != 200:
                    logger.error(f"ElevenLabs synthesis failed: {response.status_code} - {response.text}")
                    response.raise_for_status()
                    
                return response.content

        except httpx.TimeoutException:
            logger.error("ElevenLabs synthesis timed out after 90s.")
            raise Exception("Provider synthesis timeout")
        except Exception as e:
            logger.error(f"ElevenLabs TTS Synthesis failed: {str(e)}")
            raise e
