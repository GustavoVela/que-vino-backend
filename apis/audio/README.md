# Audio Generation API (Que Vino!?)

Gateway unificado de generación de audio (TTS) para el ecosistema de agentes de Que Vino!?, integrando ElevenLabs, Google Cloud TTS y enriquecimiento contextual con Gemini.

## 🚀 Propósito
Facilitar la creación de contenido auditivo premium (asesoría, noticias, catas) mediante una interfaz consistente que soporta múltiples proveedores y auditoría inmutable en Google Cloud.

## 🏗 Arquitectura
Implementado como un **Micro-Swarm** independiente en Google Cloud Run, siguiendo la [Constitución del Proyecto](file:///.specify/memory/constitution.md).

### Componentes Clave:
*   **Gemini 1.5 Flash:** Actúa como "Director de Orquesta" para inyectar etiquetas expresivas o SSML según el proveedor.
*   **ElevenLabs:** Generación de voces premium con alta expresividad.
*   **Google Cloud TTS:** Generación robusta y escalable con voces neuronales.
*   **GCS Storage:** Persistencia centralizada en `gs://{PROJECT_ID}-media/audio/`.
*   **BigQuery:** Registro de auditoría en `src_api_transactions.audio_generation_log`.

## 🛠 Instalación y Uso

### Variables de Entorno (.env)
```env
GEMINI_AUDIO_API_KEY="..."
ELEVENLABS_AUDIO_API_KEY="..."
GCS_AUDIO_BUCKET_NAME="que-vino-23032025-media"
DEFAULT_VOICE_ELEVENLABS="21m00Tcm4TDOqjz76jtA"
DEFAULT_VOICE_GOOGLE="es-US-Neural2-A"
```

### Ejecución Local
```bash
poetry install
poetry run uvicorn main:app --reload --port 8001
```

## 📡 Endpoints (Tools para Agentes)

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `POST` | `/audio/generate` | Genera audio a partir de texto con soporte para IA y múltiples proveedores. |
| `GET` | `/audio/voices` | Lista las voces disponibles de todos los proveedores activos (Resiliente). |
| `GET` | `/audio/models` | Consulta modelos y configuraciones de ElevenLabs. |

## 🛡 Seguridad (CORS)
Solo permite orígenes del ecosistema (localhost, quevino.mx, lovable.app) definidos en la sección 4.2 de la constitución.

## 📜 Licencia
Propiedad de Que Vino!? - Todos los derechos reservados.
