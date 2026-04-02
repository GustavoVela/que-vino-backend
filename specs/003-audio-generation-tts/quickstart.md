# Quickstart: Generación de Audio Multi-Proveedor (TTS API)

**Feature**: `003-audio-generation-tts`
**Status**: Ready for Implementation

## Prerequisites
- **Python 3.12+**
- **Google Cloud SDK** (Auth with `gcloud auth application-default login`)
- **ElevenLabs API Key**: Required for provider `ELEVENLABS`.

## Environment Variables (.env)
```env
PROJECT_ID="que-vino-prd"
GCS_BUCKET_NAME="que-vino-23032025-audios"
ELEVENLABS_API_KEY="[SECRET_MANAGER:que-vino-audio-secrets:elevenlabs-key]"
GEMINI_API_KEY="[SECRET_MANAGER:que-vino-audio-secrets:gemini-key]"
GOOGLE_APPLICATION_CREDENTIALS="[path/to/credentials.json]"
```

## Setup & Running Locally
1. **Clone & CD**:
   ```bash
   cd apis/audio/
   ```
2. **Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run Dev Server**:
   ```bash
   uvicorn main:app --reload --port 8083
   ```

## Local Testing
### 1. List Voices
```bash
curl -X GET "http://localhost:8083/audio/providers/voices" -H "Authorization: Bearer [FIREBASE_ID_TOKEN]"
```

### 2. Generate Audio
```bash
curl -X POST "http://localhost:8083/audio/generate" \
     -H "Authorization: Bearer [FIREBASE_ID_TOKEN]" \
     -H "Content-Type: application/json" \
     -d '{
           "text": "Bienvenidos a Que Vino, disfruten de su copa.",
           "provider": "ELEVENLABS",
           "voice_id": "rachel",
           "output_format": "mp3",
           "enrich_audio": true
         }'
```

## Infrastructure Setup
### GCS Bucket
Crear el bucket `que-vino-23032025-audios` y definir una Lifecycle Rule para pasar a Coldline tras 90 días.

### BigQuery Dataset
Asegurarse que el dataset `src_api_transactions` existe y tiene permisos para el Service Account.
