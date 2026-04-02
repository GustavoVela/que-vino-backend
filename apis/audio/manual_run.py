import asyncio
import os
import sys
from services.audio_service import audio_service

async def manual_generation(text, enrich):
    from config import settings
    # 0. Discovery
    print(f"--- Descubriendo Voces ElevenLabs ---")
    voices = await audio_service.get_all_voices()
    eleven_voices = [v for v in voices if v["provider"] == "ELEVENLABS"]
    if not eleven_voices:
        print("Fallo: No se encontraron voces en ElevenLabs.")
        return
    
    # Try Rachel, fallback to first
    target_voice = "21m00Tcm4TDOqjz76jtA" 
    exists = any(v["voice_id"] == target_voice for v in eleven_voices)
    if not exists:
        target_voice = eleven_voices[0]["voice_id"]
        print(f"Rachel no encontrada. Usando voz fallback: {eleven_voices[0]['name']} ({target_voice})")
    else:
        print(f"Usando voz: Rachel ({target_voice})")

    print(f"--- Generación {'Enriquecida' if enrich else 'Simple'} ---")
    provider = "ELEVENLABS"
    voice_id = target_voice
    output_format = "mp3"
    user_id = "test-user-gustavo"
    transaction_id = "manual-trial-001"

    try:
        # 1. Generate
        audio_bytes, metadata = await audio_service.generate_audio(
            text=text,
            provider_key=provider,
            voice_id=voice_id,
            output_format=output_format,
            enrich_audio=enrich
        )
        print(f"Éxito: {len(audio_bytes)} bytes recibidos.")
        print(f"Metadata: {metadata}")
        
        # Save locally
        suffix = "enriched" if enrich else "simple"
        filename = f"/tmp/gustavo_{suffix}.mp3"
        with open(filename, "wb") as f:
            f.write(audio_bytes)
        print(f"Archivo guardado en: {filename}")

        # 2. Audit (Optional but good to test)
        await audio_service.persist_audit_async(
            audio_bytes, metadata, provider, voice_id, user_id, transaction_id
        )
        print("Auditoría en GCS y BigQuery sincronizada.")

    except Exception as e:
        print(f"Fallo: {str(e)}")

async def main():
    # 1. Simple
    await manual_generation("¡Hola Gustavo!", enrich=False)
    # 2. Enriched
    await manual_generation("¡Hola Gustavo!", enrich=True)

if __name__ == "__main__":
    # Ensure GEMINI_AUDIO_API_KEY etc are inherited from environment
    asyncio.run(main())
