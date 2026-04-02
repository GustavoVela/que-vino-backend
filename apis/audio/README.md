# 🔊 Audio Generation API (Que Vino!? TTS)

El micro-swarm de **Audio** es el motor unificado de síntesis de voz (Text-to-Speech) para la plataforma **Que Vino!?**. Este servicio centraliza la generación de audio de alta fidelidad utilizando múltiples proveedores y capacidades de enriquecimiento emocional mediante IA.

---

## 🎭 Proveedores de Voz Soportados

1. **ElevenLabs**: Ideal para narraciones ricas, matizadas y emocionales (High Fidelity).
2. **Google Cloud TTS**: Óptimo para respuestas técnicas, rápidas y estandarizadas (Standard & Neural).
3. **Gemini (Enrichment)**: Analiza el contexto emocional del texto e inyecta pausas, énfasis y variaciones tonales recomendadas.

---

## 🛠️ API REST Reference

Todas las peticiones deben incluir un **Firebase ID Token** en el header `Authorization`.

### 1. Generación de Audio (Stream)
- **POST** `/audio/generate`
- **Body**:
```json
{
  "text": "Hola, bienvenido al club de vinos Que Vino!? ¿En qué puedo ayudarte?",
  "provider": "ELEVENLABS" | "GOOGLE",
  "voice_id": "rachel" | "es-US-Neural2-A",
  "output_format": "mp3" | "wav",
  "enrich_audio": true 
}
```
- **Parámetros**:
  - `text` (string): Requerido. El mensaje a convertir en voz.
  - `provider` (string): Requerido. `ELEVENLABS` o `GOOGLE`.
  - `voice_id` (string): Requerido. ID de la voz seleccionada.
  - `output_format` (string): Opcional. Predeterminado `mp3`.
  - `enrich_audio` (boolean): Opcional. Activa el análisis de Gemini para inyectar marcadores de entonación.
- **Respuesta (201 Created)**: Byte Stream binario (Content-Type: `audio/mpeg` o `audio/wav`).
- **Headers Traceability**:
  - `X-Generation-ID`: UUID único de la generación, guardado en GCS para auditoría.
  - `X-Enrichment-Status`: `ENABLED` | `FAILED` | `DISABLED`.

### 2. Listar Voces Unidas
- **GET** `/audio/providers/voices`
- **Header**: `Authorization: Bearer <ID_TOKEN>`
- **Descripción**: Expone un catálogo unificado de voces de ElevenLabs y Google mapeadas bajo un esquema común de género y estilo.
- **Respuesta**:
```json
[
  { "id": "rachel", "provider": "ELEVENLABS", "gender": "Female", "description": "Bright, clear for narration", "language": "es" },
  { "id": "es-US-Neural2-A", "provider": "GOOGLE", "gender": "Female", "description": "Standard neural for technical responses", "language": "es" }
]
```

### 3. Salud del Servicio
- **GET** `/health`
- **Respuesta**: `{"status": "ok", "service": "que-vino-audio-api"}`

---

## 🕵️ Auditoría y Persistencia

Siguiendo la **Sección 6.192 de la Constitución de Que Vino!?**:
- Cada audio generado se persiste automáticamente en un bucket de **GCS** (`que-vino-[ID]-media/audio`).
- Cada transacción se registra en **BigQuery** (`src_api_transactions.audio_generation_log`).

---

## 🔒 Autenticación (Auth)

El microservicio utiliza **Firebase Authentication**.

**Token URL**: `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[FIREBASE_API_KEY]`

---

## ⚙️ Configuración (Environment)

Asegúrate de configurar las siguientes variables en el `.env` o en Cloud Run:
- `GEMINI_AUDIO_API_KEY`: Para el enriquecimiento emocional.
- `ELEVENLABS_AUDIO_API_KEY`: API Key de ElevenLabs.
- `GCS_AUDIO_BUCKET_NAME`: Bucket de salida para auditoría.

---

## 📦 Desarrollo y Despliegue

```bash
# Ejecución Local
python main.py

# Despliegue Cloud Run (Usa Cloud Build)
gcloud builds submit --config deploy/cloudbuild.yaml .
```

---
© 2026 Que Vino!? - Constitución y Reglas de Agentic Architecture.
