# Implementation Plan: Gestión de Base de Conocimiento RAG (Knowledge Stores)

**Branch**: `002-rag-knowledge-base` | **Date**: 2026-03-31 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-rag-knowledge-base/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Implementación de un sistema de gestión de repositorios de conocimiento para RAG (Knowledge Stores) en "Que Vino!?". La API permitirá sincronizar de forma incremental el contenido de buckets de Google Cloud Storage (GCS) con Gemini Knowledge Stores mediante una lógica de "espejo" (mirroring), optimizando costos al comparar el tamaño de los archivos. El sistema incluye autenticación obligatoria vía Firebase y auditoría asíncrona de todas las transacciones en BigQuery.

## Technical Context

**Language/Version**: Python 3.12+
**Primary Dependencies**: FastAPI, Pydantic, google-cloud-storage, google-cloud-bigquery, google-generativeai
**Storage**: Google BigQuery (Primary DB), Google Cloud Storage (Source)
**Testing**: Pytest
**Target Platform**: Google Cloud Run
**Project Type**: Web Service (FastAPI)
**Performance Goals**: < 500ms P95 para listados (SC-002); Sync eficiente omitiendo archivos duplicados.
**Constraints**: Autenticación Google/Firebase obligatoria; Auditoría asíncrona (BackgroundTasks); No modificar GCS (Solo lectura).
**Scale/Scope**: Microservicio independiente `apis/knowledge_stores`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Python 3.12+ (Strict typing).
- [x] FastAPI (Tools & Agents exposure).
- [x] Poetry (Package management).
- [x] BigQuery ONLY (No other DB/cache).
- [x] Cloud Run Deployment (Autonomous unit).
- [x] Google Auth (Firebase tokens).
- [x] Spanish comments/docs, English code.
- [x] Detailed error handling (JSON format).
- [x] BigQuery Partitioning & Clustering defined in schemas.

## Project Structure

### Documentation (this feature)

```text
specs/002-rag-knowledge-base/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
apis/knowledge_stores/
├── main.py              # FastAPI endpoints
├── mcp_server.py        # MCP exposure for Agents
├── config.py            # Local configuration
├── core/                # Shared logic (auth, db)
│   ├── auth_middleware.py
│   ├── db.py
│   └── gemini_client.py
├── schemas/             # BQ schemas & Pydantic models
│   ├── api_models.py
│   └── bq_schemas.py
├── tests/               # Pytest isolated tests
└── deploy/              # Cloud Run / Docker files
```

**Structure Decision**: El proyecto sigue el patrón de microservicios autónomos definido en la Constitución, ubicando la nueva API en `apis/knowledge_stores/`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
