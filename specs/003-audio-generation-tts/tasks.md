# Task Breakdown: Generación de Audio Multi-Proveedor (TTS API)

**Branch**: `003-audio-generation-tts` | **Status**: Completed | **Date**: 2026-04-01
**Source Documents**: [spec.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/specs/003-audio-generation-tts/spec.md), [plan.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/specs/003-audio-generation-tts/plan.md), [research.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/specs/003-audio-generation-tts/research.md)

## Phase 1: Setup & Constitutional Standards (Project Initialization)
*Goal: Initialize the microservice directory, dependencies and basic hosting configuration.*

- [x] T001 Create directory structure for `apis/audio/` as defined in `plan.md`
- [x] T002 Migración a Poetry (`pyproject.toml`). (SECCIÓN 1.11).
- [x] T003 Create `apis/audio/deploy/Dockerfile` for Cloud Run (Python 3.12, Poetry, non-root user). (SECCIÓN 7.197).
- [x] T004 [P] Create `apis/audio/README.md` with service-specific operational documentation

## Phase 2: Foundational (Cross-cutting Concerns)
*Goal: Implement shared infrastructure services (Config, Auth, BQ, Logger).*

- [x] T005 [P] Implement `apis/audio/config.py` in root using Pydantic Settings. (SECCIÓN 2.3).
- [x] T006 Implement `apis/audio/core/logger.py` with standard JSON formatting for Cloud Logging
- [x] T007 Implement `apis/audio/core/db.py` for asynchronous BigQuery logging and timeout management
- [x] T008 [P] Implement `apis/audio/schemas/bq_models.py` defining BigQuery Pydantic schemas for logs. (SECCIÓN 2.3).

## Phase 3: [US1] Authentication & Identity Delegation
*Goal: Ensure only authorized users consume TTS resources and update player profile.*

- [x] T009 [US1] Implement `apis/audio/core/auth_middleware.py` for Firebase JWT validation (Reuse standard logic)
- [x] T010 [P] [US1] Implement Auth tracking in `main.py` using BigQuery `authentication_log`
- [x] T011 [US1] Verify that `AuthMiddleware` correctly upserts user profile in BigQuery `src_database.users`

## Phase 4: [US2] Unified Voice & Model Catalogs
*Goal: Expose standardized endpoints to list voices and models from both providers.*

- [x] T012 [US2] Implement `apis/audio/services/providers/base.py` Abstract Base Class `TTSProvider`
- [x] T013 [P] [US2] Implement `apis/audio/services/providers/google_tts.py` specifically for voice enumeration
- [x] T014 [US2] Implement `apis/audio/services/providers/elevenlabs.py` for listing voices and mapping to standard schema
- [x] T015 [P] [US2] Implement `apis/audio/services/audio_service.py` to unify catalog results with 24h In-memory cache
- [x] T016 [US2] Expose `GET /audio/providers/voices` and `GET /audio/providers/models` in `main.py`
- [x] T016.b Implementación de Capa Agéntica (`mcp_server.py`). (SECCIÓN 2.4).

## Phase 5: [US3] Audio Synthesis, Gemini Enrichment & GCS Persistence
*Goal: Core flow to generate audio, enrich with Gemini, and store in GCS for audit.*

- [x] T017 [US3] Implement `apis/audio/services/gemini_service.py` con SDK `google-genai` v1.70.0+ y Prompts en Markdown. (SECCIÓN 1.16 / 10).
- [x] T018 [P] [US3] Implement `apis/audio/services/gcs_service.py` for immutable uploads and metadata tagging (No signed URLs needed in response)
- [x] T019 [US3] Finalize `apis/audio/services/providers/google_tts.py` for SSML synthesis
- [x] T020 [US3] Finalize `apis/audio/services/providers/elevenlabs.py` for Tag-based synthesis
- [x] T021 [US3] Coordinate generation flow in `AudioService` (Handle `SUCCESS_WITHOUT_ENRICHMENT` if Gemini fails)
- [x] T022 [US3] Implement `POST /audio/generate` returning **Binary Stream** + Headers (`X-Generation-ID`, `X-Enrichment-Status`)
- [x] T023 [US3] Ensure `AudioService` uses `BackgroundTasks` for GCS and BQ logging for audit

## Phase 6: [US4] Error Handling & Observability
*Goal: Graceful degradation and specific error codes (402, 502).*

- [x] T024 [P] [US4] Implement global exception handler in `main.py` mapping provider errors to standard HTTP codes
- [x] T025 [US4] Implement `status` tracking in `audio_generation_log` (e.g. `SUCCESS_WITHOUT_ENRICHMENT`, `ERROR_OUT_OF_CREDITS`)
- [x] T026 [P] [US4] Finalize logic for "Graceful Degradation" if Gemini fails (fallback to raw text synthesis)

## Phase 7: Polish & Readiness
*Goal: Final validation against specification and documentation cleanup.*

- [x] T027 Run integration tests against mocked providers to verify GCS/BQ synchronization
- [x] T028 Update `OPENCLAW_TOOLS.md` with the new TTS API documentation for Agent use
- [x] T029 Clean up any temporary debug logs and finalize `apis/audio/README.md` endpoints list

## Dependencies & Strategy
- **MVP Scope**: Phases 1-5 (Initial generation with fixed provider and 1 voice).
- **Execution Strategy**: Parallelize foundational tasks (T005-T008) while designing the abstract provider layer.
- **Independent Testing**: Each User Story phase generates a complete, testable API interaction.
