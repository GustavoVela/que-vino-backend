# Implementation Plan: Generación de Audio Multi-Proveedor (TTS API)

**Branch**: `003-audio-generation-tts` | **Date**: 2026-04-01 | **Spec**: [spec.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/specs/003-audio-generation-tts/spec.md)
**Input**: Feature specification from `/specs/003-audio-generation-tts/spec.md`

## Summary

Implementación de un microservicio unificado de Generación de Audio (TTS) en Cloud Run que actúa como Gateway para ElevenLabs y Google Cloud TTS. El sistema utiliza Gemini para enriquecer el texto con etiquetas expresivas, garantiza la persistencia inmutable en Google Cloud Storage para auditoría y mantiene una trazabilidad total de transacciones en BigQuery, siguiendo estrictamente la Constitución de "Que Vino".

## Technical Context

**Language/Version**: Python 3.12+ (Constitución)  
**Primary Dependencies**: FastAPI, `google-genai` (v1.70.0+), `google-cloud-storage`, `google-cloud-bigquery`, `httpx`, `pydantic-settings`  
**Storage**: Google Cloud Storage (Bucket: `que-vino-23032025-audios`), BigQuery (`src_api_transactions`)  
**Testing**: pytest  
**Target Platform**: Google Cloud Run  
**Project Type**: Web Service (Microservice)  
**Performance Goals**: < 300ms utilería (caché), < 2.0s generación (p95 incluyendo Gemini)  
**Constraints**: Firebase Auth mandatorio, BQ timeout 5s, Secret Manager para llaves de API  
**Scale/Scope**: Micro-swarm independiente bajo `/apis/audio/`

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Standard Compliance
- [x] **Firebase Auth**: Implementación vía `AuthMiddleware` en `core/`.
- [x] **BigQuery Logging**: Uso de `log_event_async` para auditoría y `audio_api_log`.
- [x] **Secret Manager**: Carga de `ELEVENLABS_API_KEY` y `GOOGLE_APPLICATION_CREDENTIALS`.
- [x] **Python 3.12**: Confirmado en `Dockerfile` y configuración de entorno.
- [x] **Async Architecture**: Uso de `BackgroundTasks` para logging y escritura en GCS para no bloquear la respuesta al cliente.

## Project Structure

### Documentation (this feature)

```text
specs/003-audio-generation-tts/
├── plan.md              # Este archivo
├── research.md          # Fase 0: Decisiones técnicas sobre SSML y IAM
├── data-model.md        # Fase 1: Esquemas de BigQuery y GCS
├── quickstart.md        # Fase 1: Guía de despliegue y pruebas
├── contracts/           # Fase 1: OpenAPI Spec (audio_generate.json)
└── tasks.md             # Fase 2: Breakdown detallado
```

### Source Code

```text
apis/audio/
├── main.py              # Punto de entrada FastAPI y ruteo
├── requirements.txt     # Dependencias del servicio
├── Dockerfile           # Configuración de despliegue Cloud Run
├── README.md            # Documentación técnica del servicio
├── core/
│   ├── config.py        # Configuración, Env Vars y Secret Manager
│   ├── auth_middleware.py # Validación de JWT y User Profile
│   ├── db.py            # Conector async a BigQuery
│   └── logger.py        # Logger estandarizado
├── services/
│   ├── audio_service.py # Gateway lógico (Orquestación Generación + GCS)
│   ├── gcs_service.py   # Interfaz con Cloud Storage (Append-only)
│   ├── gemini_service.py # Lógica de enriquecimiento de texto
│   └── providers/
│       ├── base.py      # Interfaz abstracta para TTS Providers
│       ├── google_tts.py # Implementación Google Cloud TTS
│       └── elevenlabs.py # Implementación ElevenLabs API
├── models/
│   ├── schemas.py       # Pydantic (Request Body, Response Model)
│   └── bq_models.py     # Definición de filas para BigQuery
└── tests/
    ├── unit/            # Pruebas de lógica de enriquecimiento y mapeo
    └── integration/     # Pruebas de API Mockeando proveedores
```

**Structure Decision**: El servicio se ubicará en `apis/audio/` operando como un microservicio independiente con su propia configuración de infraestructura, siguiendo el patrón de los servicios existentes (`knowledge_stores`, `stores`).

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Múltiples Proveedores | Flexibilidad de costes y calidad | Usar solo uno limita la calidad según el idioma |
| Inmutabilidad GCS | Requerimiento de auditoría legal | Permitir borrar audios viola la integridad del registro |

## Phase 0: Research Items

1. **Research item 1**: Límites de caracteres y compatibilidad de SSML vs etiquetas emocionales nativas de ElevenLabs para el prompt de Gemini.
2. **Research item 2**: Estrategia de caché para `GET /voices` de Google TTS (latencia excesiva en llamadas directas).
3. **Research item 3**: Configuración de política IAM mínima para el Service Account (Escritura en GCS sin permisos de borrado/listado público).
