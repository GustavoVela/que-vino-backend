# Quick Reference

This implementation involves creating two distinct business APIs under `/apis/stores/` and `/apis/locations/`.

### Development Bootstrapping

1. Use `.env` from Que Vino backend root for Firebase and BigQuery configurations.
2. Under `apis/stores/` and `apis/locations/`, run `poetry config virtualenvs.in-project true` and `poetry install` to create localized virtual environments.
3. Validate schemas: Ensure your schemas match BigQuery partitioning (1) and clustering (up to 4 keys).

### Running Microservices

**To serve the REST API locally:**
```bash
poetry run uvicorn main:app --reload
```

**To test the MCP local server:**
Use the MCP Inspector referencing the localized virtual environment:
```bash
npx @modelcontextprotocol/inspector poetry run python mcp_server.py
```

### Pre-requisites Checklist before pushing
- Run tests: `pytest tests/`
- Verify Docker configuration in `deploy/` is isolated and maps purely to the single API.
- Verify that `google-antigravity` service account is utilized.
