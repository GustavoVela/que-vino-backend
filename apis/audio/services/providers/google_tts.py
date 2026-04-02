from google.cloud import texttospeech
from .base import TTSProvider
from typing import List, Dict, Any


class GoogleTTSProvider(TTSProvider):
    def __init__(self, project_id: str):
        self.client = texttospeech.TextToSpeechClient()
        self.project_id = project_id

    def provider_name(self) -> str:
        return "GOOGLE"

    async def list_voices(self) -> List[Dict[str, Any]]:
        """List and map Google voices to standard format."""
        try:
            voices = self.client.list_voices()
            standardized = []
            for voice in voices.voices:
                standardized.append({
                    "provider": self.provider_name(),
                    "voice_id": voice.name,
                    "name": voice.name,
                    "languages": list(voice.language_codes),
                    "ssml_gender": texttospeech.SsmlVoiceGender(voice.ssml_gender).name,
                    "natural_sample_rate_hertz": voice.natural_sample_rate_hertz
                })
            return standardized
        except Exception:
            return []

    async def list_models(self) -> List[Dict[str, Any]]:
        """Google models are usually tied to voice technology."""
        return [
            {"provider": self.provider_name(), "model_id": "journey", "name": "Google Journey (Premium)"},
            {"provider": self.provider_name(), "model_id": "studio", "name": "Google Studio (High-Fidelity)"},
            {"provider": self.provider_name(), "model_id": "wavenet", "name": "Google WaveNet (Neural)"},
            {"provider": self.provider_name(), "model_id": "standard", "name": "Google Standard"}
        ]

    async def synthesize(self, text: str, voice_id: str, output_format: str, **kwargs) -> bytes:
        """Execute Google TTS Synthesis."""
        try:
            # Detect if it's SSML or plain text
            is_ssml = text.strip().startswith("<speak>") or text.strip().startswith("<xml")
            
            if is_ssml:
                synthesis_input = texttospeech.SynthesisInput(ssml=text)
            else:
                synthesis_input = texttospeech.SynthesisInput(text=text)

            # Build the voice request
            # voice_id for Google is 'en-US-Standard-A', etc.
            # language_code extracted from first part
            lang_code = "-".join(voice_id.split("-")[:2])
            
            voice = texttospeech.VoiceSelectionParams(
                name=voice_id,
                language_code=lang_code
            )

            # Audio Config (Gateway standardized)
            audio_encoding = texttospeech.AudioEncoding.MP3
            if output_format == "wav":
                audio_encoding = texttospeech.AudioEncoding.LINEAR16

            audio_config = texttospeech.AudioConfig(
                audio_encoding=audio_encoding
            )

            # Perform the request
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )

            return response.audio_content

        except Exception as e:
            from core.logger import logger
            logger.error(f"Google TTS Synthesis failed: {str(e)}")
            raise e
