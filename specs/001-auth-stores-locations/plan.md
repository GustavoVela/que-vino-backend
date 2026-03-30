# Implementation Plan: 001-que-vino-auth-stores-y-locations

**Branch**: `001-auth-stores-locations` | **Date**: 2026-03-29 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-auth-stores-locations/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

The feature provides a scalable and secure backend to manage Wine Stores (CRUD) and their Locations, exposed via standard REST APIs (FastAPI) and identically via MCP (Model Context Protocol) for AI Agents. It implements Firebase Auth validation, robust synchronous BigQuery logging for critical data modifications, and asynchronous logging for authentication, conforming strictly to the project's event-driven and microservices architectural patterns on Cloud Run.

## Technical Context

**Language/Version**: Python 3.12+ (Strict typing)
**Primary Dependencies**: FastAPI, Google Cloud BigQuery, Firebase Admin SDK, MCP Python SDK, Pydantic, Poetry
**Storage**: Google BigQuery (Exclusively: `src_database.*` and `src_api_transactions.*`)
**Testing**: pytest
**Target Platform**: Google Cloud Run (Serverless) via Cloud Build
**Project Type**: Web Service API (REST) & MCP Server
**Performance Goals**: < 250ms p95 latency for GET/Search endpoints, immediate response for Auth (async logging).
**Constraints**: Synchronous logging to BigQuery for all CRUD operations before returning HTTP response.
**Scale/Scope**: Internal Admin usage + AI Agent delegated consumption. Strict Anti-Prompt Injection guardrails.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Tech Stack**: Uses Python 3.12, FastAPI, Poetry, BigQuery, and Cloud Run.
- [x] **No Caches/Relational DBs**: Storage is strictly BigQuery.
- [x] **Architecture**: Microservice format exposing `main.py` (REST) and `mcp_server.py` (Agent tools).
- [x] **BigQuery Schema**: Declarative schemas with proper Partitioning (1 key) and Clustering (up to 4 keys).
- [x] **Logging**: Dedicated append-only log tables (`stores_log`, `locations_log`, `authentication_log`).
- [x] **Security**: Firebase Auth JWT verification and Regex allow-lists for MCP tools.
- [x] **Testing & Deploy**: Isolated `/tests/` and `/deploy/` folders per microservice.

## Project Structure

### Documentation (this feature)

```text
specs/001-auth-stores-locations/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
apis/
├── stores/
│   ├── config.py
│   ├── main.py              # Capa de API tradicional REST/FastAPI (Admin)
│   ├── mcp_server.py        # Exposición MCP para Agentes
│   ├── schemas/             # Definiciones BigQuery (stores, stores_log)
│   ├── tests/
│   └── deploy/
│       ├── Dockerfile
│       └── cloudbuild.yaml
└── locations/
    ├── config.py
    ├── main.py              # Capa de API tradicional REST/FastAPI
    ├── mcp_server.py        # Exposición MCP para Agentes
    ├── schemas/             # Definiciones BigQuery (locations, locations_log)
    ├── tests/
    └── deploy/
        ├── Dockerfile
        └── cloudbuild.yaml
```

**Structure Decision**: A dual microservice topology is chosen mapping to `apis/stores/` and `apis/locations/` as per the constitution's component autonomy rule (Section 2.1). Each handles its own schemas, endpoints, tests, and deployment lifecycle.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A | N/A | N/A |
