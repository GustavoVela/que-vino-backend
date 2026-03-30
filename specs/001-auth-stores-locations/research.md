# Phase 0: Outline & Research

## Dependencies & Integrations

- **Decision**: Use FastAPI for both standard endpoints and MCP exposure.
- **Rationale**: Standardizes API development, fully supported natively by the MCP Python SDK, aligns with the constitution.
- **Alternatives considered**: Separate frameworks for MCP and API or raw Python scripts.

- **Decision**: Use BigQuery as the exclusive Datastore.
- **Rationale**: Fully compliant with the constitution rule indicating no PostgreSQL/Redis caching mechanism.
- **Alternatives considered**: PostgreSQL for traditional CRUD, but discarded due to explicit architectural directives.

- **Decision**: Synchronous vs Asynchronous Logging for CRUD vs Auth.
- **Rationale**: Preserves data trace integrity (CRUD is critical, so synchronous) vs UX (Auth requires quick render, so asynchronous).
- **Alternatives considered**: Fully asynchronous logging, discarded because mutating critical data requires bulletproof audit logs on BigQuery before confirming to the client.
