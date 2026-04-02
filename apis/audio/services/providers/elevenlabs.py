import httpx
from typing import List, Dict, Any
from .base import TTSProvider


class ElevenLabsProvider(TTSProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {"xi-api-key": self.api_key}

    def provider_name(self) -> str:
        return "ELEVENLABS"

    async def list_voices(self) -> List[Dict[str, Any]]:
        """List and map ElevenLabs voices to standard format."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/voices", headers=self.headers)
                response.raise_for_status()
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
        except Exception:
            return []

    async def list_models(self) -> List[Dict[str, Any]]:
        """List available ElevenLabs models."""
        try:
             async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/models", headers=self.headers)
                response.raise_for_status()
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
        except Exception:
            return []

    async def synthesize(self, text: str, voice_id: str, output_format: str, **kwargs) -> bytes:
        """Execute ElevenLabs TTS Synthesis."""
        try:
            # Map standard formats to ElevenLabs specific IDs
            # Typical: mp3_44100_128, pcm_44100
            el_format = "mp3_44100_128" if output_format == "mp3" else "pcm_44100"
            
            async with httpx.AsyncClient() as client:
                url = f"{self.base_url}/text-to-speech/{voice_id}"
                
                # Payload according to ElevenLabs docs
                payload = {
                    "text": text,
                    "model_id": kwargs.get("model_id", "eleven_multilingual_v2")
                }
                
                params = {"output_format": el_format}
                
                response = await client.post(
                    url, 
                    json=payload, 
                    headers=self.headers, 
                    params=params,
                    timeout=60.0 # Audio generation is slow
                )
                
                response.raise_for_status()
                return response.content

        except Exception as e:
            from core.logger import logger
            logger.error(f"ElevenLabs TTS Synthesis failed: {str(e)}")
            raise e
