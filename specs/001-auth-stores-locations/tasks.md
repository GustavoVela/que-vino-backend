# Tasks: 001-que-vino-auth-stores-y-locations

**Input**: Design documents from `/specs/001-auth-stores-locations/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/api.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Tests are included as per standard TDD definitions.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the dual microservice architecture.

- [X] T001 Create structural directories `apis/stores` and `apis/locations`
- [X] T002 Initialize isolated Poetry environments in `apis/stores` and `apis/locations`
- [X] T003 [P] Add dependencies (fastapi, uvicorn, google-cloud-bigquery, firebase-admin, mcp) to `apis/stores/pyproject.toml`
- [X] T004 [P] Add dependencies (fastapi, uvicorn, google-cloud-bigquery, firebase-admin, mcp) to `apis/locations/pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T005 Create `apis/stores/config.py` and `apis/locations/config.py` to load Environment vars.
- [X] T006 Setup BigQuery connection helper in `apis/stores/core/db.py` imponiendo un timeout duro de 5 segundos.
- [X] T007 [P] Setup BigQuery connection helper en `apis/locations/core/db.py` imponiendo un timeout duro de 5 segundos.
- [X] T007a [P] Implementar Rate Limiting Middleware (100 req/min -> 429) para ambas APIs en la capa `core/`.

---

## Phase 3: User Story 1 - Autenticación, Acceso a APIs y Sincronización de Usuarios (Priority: P0) 🎯 MVP

**Goal**: Establish a unified security barrier validating Firebase JWTs while maintaining async logs globally for all APIs.

**Independent Test**: Simulate an API call with an invalid token and retrieve exactly a `401 Unauthorized`. With a valid token, BigQuery `authentication_log` triggers an append.

### Tests for User Story 1
- [X] T008 [P] [US1] Integration tests for Auth middleware evaluating Valid/Invalid tokens in `apis/stores/tests/test_auth.py`
- [X] T009 [P] [US1] Integration tests for Auth middleware evaluating Valid/Invalid tokens in `apis/locations/tests/test_auth.py`

### Implementation for User Story 1
- [X] T010 [US1] Create BigQuery declarative schema properties for `users` and `authentication_log` in `apis/stores/schemas/users.py` and `apis/locations/schemas/users.py`
- [X] T011 [US1] Implement `verify_firebase_token` middleware using `BackgroundTasks` for async logging in `apis/stores/core/auth_middleware.py`
- [X] T012 [P] [US1] Implement identical `verify_firebase_token` middleware for `apis/locations/core/auth_middleware.py`

---

## Phase 4: User Story 2 - Ingesta y Actualización de Tiendas (CRUD Seguro) (Priority: P1)

**Goal**: Full CRUD manipulation of Wine Stores via REST and MCP, tracking every mutation synchronously.

**Independent Test**: Send a POST request to `/stores` and verify that both `src_database.stores` and `src_api_transactions.stores_log` are atomically populated.

### Tests for User Story 2
- [X] T013 [P] [US2] Contract testing for Store CRUD endpoints in `apis/stores/tests/test_stores_mutations.py`

### Implementation for User Story 2
- [X] T014 [US2] Create BigQuery schemas for `stores` and `stores_log` ensuring max 4 clustering fields in `apis/stores/schemas/stores.py`
- [X] T015 [P] [US2] Implement REST mutation endpoints (POST, PUT, DELETE) integrating `auth_middleware` en `apis/stores/main.py`.
- [X] T016 [P] [US2] Implement corresponding MCP tools (`create_store`, `update_store`, `delete_store`) sharing business logic inside `apis/stores/mcp_server.py`.

---

## Phase 5: User Story 3 - Listado, Búsqueda Avanzada y Paginación (Priority: P1)

**Goal**: Provide resilient reading interfaces for `stores` enforcing normalization, accent filtering, and pagination.

**Independent Test**: Request `GET /stores/search?name=viñedo` and expect items containing 'vinedo' via fast normalized query.

### Tests for User Story 3
- [X] T017 [P] [US3] Unit testing for search criteria normalizer and pagination limites (OOM limit <= 100 y 422 Rejection) en `apis/stores/tests/test_stores_queries.py`

### Implementation for User Story 3
- [X] T018 [US3] Implement list and search GET REST endpoints in `apis/stores/main.py`.
- [X] T019 [US3] Implement corresponding MCP tools (`list_stores`, `search_stores`) in `apis/stores/mcp_server.py`.

---

## Phase 6: User Story 4 - Gestión del Catálogo de Localizaciones (Priority: P2)

**Goal**: Expose an exact equivalent CRUD + Search functionality for Geographic Locations mapping to `src_database.locations`.

**Independent Test**: Add/Read Locations ensuring `locations_log` records all activities synchronously.

### Tests for User Story 4
- [X] T020 [P] [US4] Contract and Integration tests for Locations HTTP and tools in `apis/locations/tests/test_locations.py`

### Implementation for User Story 4
- [X] T021 [US4] Create declarative BigQuery schemas for `locations` and `locations_log` inside `apis/locations/schemas/locations.py`
- [X] T022 [US4] Build full REST API mapping (GET, POST, PUT, DELETE) in `apis/locations/main.py`.
- [X] T023 [US4] Build standard MCP tool mapping in `apis/locations/mcp_server.py`.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect deployment and ecosystem visibility.

- [X] T024 [P] Create decoupled `Dockerfile` and `cloudbuild.yaml` in `apis/stores/deploy/` and `apis/locations/deploy/` using the `google-antigravity` SA.
- [X] T025 Documentation updates in `apis/stores/README.md` and `apis/locations/README.md` appending exact running cURLs as ordered by the constitution.
- [X] T026 Update `OPENCLAW_TOOLS.md` at project root with the productive paths of the newly introduced stores and locations services.
- [X] T027 Run MCP local validation to ensure complete absence of generic failure logs.
- [X] T028 [P] Escribir pruebas automatizadas simulando ataques de Prompt Injection (SQLi) hacia las herramientas expuestas en `mcp_server.py` comprobando validación Regex segura.

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: No dependencies - can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational. Because `apis/stores/` and `apis/locations/` are decoupled, US1 to US3 (stores) can start entirely concurrently with US4 (locations) given an independent developer.

### Parallel Opportunities
- Microservice scaffolding (Phase 1 and 2) can easily be achieved concurrently.
- User Story 4 (Locations) can be developed strictly in parallel with User Story 2 & 3 (Stores) because there is no domain friction.
- Documentation and Deploy configuration updates at Phase 7 are also standalone and parallelizable.
