from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class TTSProvider(ABC):
    @abstractmethod
    def provider_name(self) -> str:
        """Name of the provider (e.g. ELEVENLABS, GOOGLE)"""
        pass

    @abstractmethod
    async def list_voices(self) -> List[Dict[str, Any]]:
        """List all available voices standardized."""
        pass

    @abstractmethod
    async def list_models(self) -> List[Dict[str, Any]]:
        """List all available models standardized."""
        pass

    @abstractmethod
    async def synthesize(
        self, 
        text: str, 
        voice_id: str, 
        output_format: str, 
        **kwargs
    ) -> bytes:
        """Perform TTS synthesis and return bytes."""
        pass
