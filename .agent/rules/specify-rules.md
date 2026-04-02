# que-vino-backend Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-01

## Active Technologies
- Python 3.12+ + FastAPI, Pydantic, google-cloud-storage, google-cloud-bigquery, google-generativeai (002-rag-knowledge-base)
- Google BigQuery (Primary DB), Google Cloud Storage (Source) (002-rag-knowledge-base)
- Python 3.12+ (Constitución) + FastAPI, `google-genai` (v1.70.0+), `google-cloud-storage`, `google-cloud-bigquery`, `httpx`, `pydantic-settings` (003-audio-generation-tts)
- Google Cloud Storage (Bucket: `que-vino-23032025-audios`), BigQuery (`src_api_transactions`) (003-audio-generation-tts)

- Python 3.12+ (Strict typing) + FastAPI, Google Cloud BigQuery, Firebase Admin SDK, MCP Python SDK, Pydantic, Poetry (001-auth-stores-locations)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.12+ (Strict typing): Follow standard conventions

## Recent Changes
- 003-audio-generation-tts: Added Python 3.12+ (Constitución) + FastAPI, `google-genai` (v1.70.0+), `google-cloud-storage`, `google-cloud-bigquery`, `httpx`, `pydantic-settings`
- 002-rag-knowledge-base: Added Python 3.12+ + FastAPI, Pydantic, google-cloud-storage, google-cloud-bigquery, google-generativeai

- 001-auth-stores-locations: Added Python 3.12+ (Strict typing) + FastAPI, Google Cloud BigQuery, Firebase Admin SDK, MCP Python SDK, Pydantic, Poetry

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
