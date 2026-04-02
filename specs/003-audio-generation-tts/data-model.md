# Data Model: Generación de Audio Multi-Proveedor (TTS API)

**Feature**: `003-audio-generation-tts`
**Source**: [spec.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/specs/003-audio-generation-tts/spec.md)

## BigQuery Tables (Dataset: `src_api_transactions`)

### 1. `audio_api_log` (Low-Level Traffic Audit)
| Column | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `transaction_id` | STRING | REQUIRED | UUID v4 (Primary Key). |
| `performed_by_user_id` | STRING | NULLABLE | Firebase UID. |
| `transaction_api_type` | STRING | REQUIRED | 'GET' \| 'POST'. |
| `transaction_api_path` | STRING | REQUIRED | Endpoint path called. |
| `transaction_parameters` | JSON | NULLABLE | Query params. |
| `payload_request` | JSON | NULLABLE | Raw request body. |
| `payload_response` | JSON | NULLABLE | Raw response body (meta or error). |
| `event_timestamp` | TIMESTAMP | REQUIRED | Server execution time (UTC). |
| `ingestion_timestamp` | TIMESTAMP | REQUIRED | BQ partition key. |

- **Partitioning**: `ingestion_timestamp` (MONTHLY - Optimized for audit costs).
- **Clustering**: `transaction_api_path`, `performed_by_user_id`.

### 2. `audio_generation_log` (Bussiness & AI Audit)
| Column | Type | Mode | Description |
| :--- | :--- | :--- | :--- |
| `generation_id` | STRING | REQUIRED | UUID v4 (Filename in GCS). |
| `api_transaction_id` | STRING | REQUIRED | FK to `audio_api_log`. |
| `performed_by_user_id` | STRING | REQUIRED | Requesting user. |
| `provider` | STRING | REQUIRED | 'ELEVENLABS' \| 'GOOGLE'. |
| `voice_id` | STRING | REQUIRED | Voice identifier used. |
| `is_enriched` | BOOLEAN | REQUIRED | If Gemini enrichment applied. |
| `text_input` | STRING | REQUIRED | Original source text. |
| `text_processed` | STRING | NULLABLE | Text after Gemini (if applicable). |
| `status` | STRING | REQUIRED | 'SUCCESS' \| 'SUCCESS_WITHOUT_ENRICHMENT' \| 'ERROR_OUT_OF_CREDITS' \| 'FAIL'. |
| `event_timestamp` | TIMESTAMP | REQUIRED | UTC server time. |
| `ingestion_timestamp` | STRING | REQUIRED | BQ partition key. |

- **Partitioning**: `ingestion_timestamp` (MONTHLY).
- **Clustering**: `provider`, `status`.

## Google Cloud Storage (Bucket: `que-vino-23032025-audios`)

### Object Structure
- **Path**: `generations/{generation_id}.{extension}` (e.g. `generations/a1b2c3d4.mp3`).
- **Metadata**: `user_id`, `provider`, `voice_id` (Injected as Custom Metadata).

### Lifecycle Policy
- **Move to Coldline**: After 90 days of creation.
- **Expiration**: None (Permanent Audit Records).

## Interface Contracts (Contracts/)

### Endpoint: `POST /audio/generate`
- **Request (JSON)**:
  ```json
  {
    "text": "Bienvenidos a Que Vino, disfruten de su copa.",
    "provider": "ELEVENLABS",
    "voice_id": "rachel_v2",
    "output_format": "mp3",
    "enrich_audio": true
  }
  ```
- **Response (201 Created)**:
  - **Body**: Archivo binario de audio (`audio/mpeg` para mp3, `audio/wav` para wav).
  - **Headers**:
    - `X-Generation-ID`: UUID v4 generado.
    - `X-Enrichment-Status`: 'SUCCESS' \| 'FAILED' \| 'SKIPPED'.
  - **Note**: No se devuelve JSON. El cliente recibe el stream directo para reproducción inmediata.
- **Error (402 Payment Required)**: Provider out of credits.
- **Error (422 Unprocessable Entity)**: Text too long or invalid provider/voice combination.
