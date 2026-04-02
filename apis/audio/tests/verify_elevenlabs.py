import sys
import os
import asyncio

# Add the current directory to sys.path to allow importing from the root of apis/audio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.providers.elevenlabs import ElevenLabsProvider
from config import settings

async def test_elevenlabs():
    print(f"Testing ElevenLabs Provider with key: {settings.ELEVENLABS_AUDIO_API_KEY[:6]}...")
    
    provider = ElevenLabsProvider(settings.ELEVENLABS_AUDIO_API_KEY)
    
    # 1. Test List Voices
    print("\n[Testing list_voices]")
    voices = await provider.list_voices()
    if voices:
        print(f"Success! Found {len(voices)} voices. First one: {voices[0]['name']} ({voices[0]['voice_id']})")
    else:
        print("Failed to list voices. Check logs.")
        
    # 2. Test List Models
    print("\n[Testing list_models]")
    models = await provider.list_models()
    if models:
        print(f"Success! Found {len(models)} models. First one: {models[0]['name']} ({models[0]['model_id']})")
    else:
        print("Failed to list models. Check logs.")
        
    # 3. Test Synthesis (Mock or real if possible)
    # We won't actually perform synthesis to save credits unless we want to, 
    # but we can verify the URL and payload logic if we mock.
    
if __name__ == "__main__":
    asyncio.run(test_elevenlabs())
