# 🔊 Audio Generation API (Que Vino!? TTS)

El micro-swarm de **Audio** es el motor unificado de síntesis de voz (Text-to-Speech) para la plataforma **Que Vino!?**. Este servicio centraliza la generación de audio de alta fidelidad utilizando múltiples proveedores y capacidades de enriquecimiento emocional mediante IA.

- **URL Producción**: `https://quevino-audio-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/audio/`
- **Resultados de Prueba**: [`tests/TEST_RESULTS.md`](tests/TEST_RESULTS.md)

---

## 🎭 Proveedores de Voz Soportados

1. **ElevenLabs**: Ideal para narraciones ricas, matizadas y emocionales (High Fidelity).
2. **Google Cloud TTS**: Óptimo para respuestas técnicas, rápidas y estandarizadas (Standard & Neural).
3. **Gemini (Enrichment)**: Analiza el contexto emocional del texto e inyecta pausas, énfasis y variaciones tonales recomendadas.

---

## 🛠️ API REST Reference

Todas las peticiones deben incluir un **Firebase ID Token** en el header `Authorization: Bearer <ID_TOKEN>`.

### 1. Generación de Audio

**POST** `/audio/generate`

```bash
curl -X POST "https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/generate" \
  -H "Authorization: Bearer <ID_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Bienvenido a Que Vino!? Tu sommelier digital.",
    "provider": "ELEVENLABS",
    "voice_id": "kh59ZgGFT1YQNe4P0U2V",
    "model_id": "eleven_multilingual_v2",
    "output_format": "mp3",
    "enrich_audio": false
  }' \
  --output audio.mp3
```

| Parámetro | Tipo | Req. | Descripción |
|---|---|---|---|
| `text` | string | ✅ | Texto a convertir en voz. |
| `provider` | string | ✅ | `ELEVENLABS` o `GOOGLE`. |
| `voice_id` | string | ✅ | ID de la voz. Obtener de `GET /audio/providers/voices`. |
| `model_id` | string | ❌ | Modelo de síntesis (ej: `eleven_multilingual_v2`, `eleven_v3`). Por defecto según proveedor. |
| `output_format` | string | ❌ | `mp3` (defecto) o `wav`. |
| `enrich_audio` | boolean | ❌ | Activa análisis de Gemini para inyectar marcadores de entonación. |

**Respuesta (201 Created)**: Byte stream binario (`audio/mpeg` o `audio/wav`).

**Headers de Trazabilidad**:
- `X-Generation-ID`: UUID único de la generación, persistido en GCS para auditoría.
- `X-Enrichment-Status`: `ENABLED` | `FAILED` | `DISABLED`.

---

### 2. Listar Voces Disponibles

**GET** `/audio/providers/voices`

```bash
curl "https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/providers/voices" \
  -H "Authorization: Bearer <ID_TOKEN>"
```

**Respuesta (200)**:
```json
[
  { "provider": "ELEVENLABS", "voice_id": "kh59ZgGFT1YQNe4P0U2V", "name": "Rachel", "languages": ["es"], "category": "premade" },
  { "provider": "GOOGLE", "voice_id": "es-US-Neural2-A", "name": "es-US-Neural2-A", "languages": ["es-US"], "ssml_gender": "FEMALE", "natural_sample_rate_hertz": 24000 }
]
```

---

### 3. Listar Modelos Disponibles

**GET** `/audio/providers/models`

```bash
curl "https://quevino-audio-2lkhisz2aa-uc.a.run.app/audio/providers/models" \
  -H "Authorization: Bearer <ID_TOKEN>"
```

---

### 4. Salud del Servicio

**GET** `/health` *(sin autenticación)*

```bash
curl "https://quevino-audio-2lkhisz2aa-uc.a.run.app/health"
# → {"status": "ok", "service": "que-vino-audio-api"}
```

---

## 🕵️ Auditoría y Persistencia

Cada audio generado se persiste automáticamente en:
- **GCS**: Bucket `que-vino-23032025-audios` (configurado en `GCS_AUDIO_BUCKET_NAME`).
- **BigQuery**: Tabla `src_api_transactions.audio_generation_log`.

---

## 🔒 Autenticación

El microservicio utiliza **Firebase Authentication**.

```bash
# Obtener Firebase ID Token
curl -X POST \
  "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=<FIREBASE_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "contraseña", "returnSecureToken": true}'
```

---

## ⚙️ Configuración (Environment)

| Variable | Descripción |
|---|---|
| `GEMINI_AUDIO_API_KEY` | API Key de Gemini para enriquecimiento emocional. |
| `ELEVENLABS_AUDIO_API_KEY` | API Key de ElevenLabs. |
| `GCS_AUDIO_BUCKET_NAME` | Bucket de GCS para persistencia de audios. |

> [!IMPORTANT]
> **Timeout de Producción**: Para evitar errores 502/504 en Cloud Run en audios largos (>30s), el servicio debe tener un timeout configurado de al menos **120 segundos**. Internamente, el microservicio maneja un timeout máximo de 90 segundos hacia los proveedores externos.

---

## 🧪 Pruebas de Integración

Ejecutar desde la raíz del repositorio:

```bash
python3 apis/audio/tests/test_production.py
```

Genera `apis/audio/tests/TEST_RESULTS.md` con el detalle de todos los llamados a producción y sus respuestas.

---

## 📦 Despliegue

```bash
# Despliegue a Cloud Run (desde el root del repositorio)
gcloud builds submit \
  --config apis/audio/deploy/cloudbuild.yaml \
  --gcs-source-staging-dir=gs://que-vino-23032025-cloudbuild/source \
  .
```

---
© 2026 Que Vino!? — Constitucion v1.5.2 | Agentic Architecture.
