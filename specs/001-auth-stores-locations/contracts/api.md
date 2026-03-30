# Interface Contracts (REST & MCP)

## Stores API

**Base URL**: `/stores`

### REST Endpoints:
- `GET /stores?page=1&limit=20`: Listed stores paginated.
- `GET /stores/search?name={string}&city={string}`: Search stores with normalized terms.
- `POST /stores`: Create store (JSON payload).
- `PUT /stores/{id}`: Edit store (JSON payload).
- `DELETE /stores/{id}`: Delete store.

### MCP Server Tools:
- `list_stores`: Maps to GET /stores
- `search_stores`: Maps to GET /stores/search
- `create_store`: Maps to POST /stores
- `update_store`: Maps to PUT /stores/{id}
- `delete_store`: Maps to DELETE /stores/{id}

---

## Locations API

**Base URL**: `/locations`

### REST Endpoints:
- `GET /locations?page=1&limit=50`: Listed locations paginated.
- `POST /locations`: Create location (JSON payload).
- `PUT /locations/{id}`: Edit location (JSON payload).
- `DELETE /locations/{id}`: Delete location.

### MCP Server Tools:
- `list_locations`: Maps to GET /locations
- `search_locations`: Exposes search functionality based on exact parameters.
- `create_location`: Maps to POST /locations
- `update_location`: Maps to PUT /locations/{id}
- `delete_location`: Maps to DELETE /locations/{id}

---

## Security Safeguards
- All operations (REST and MCP) strictly require a valid **Firebase JWT Authorization header**.
- Hard limit on string lengths: `< 50 chars`.
- Regex allow-list: `^[a-zA-Z0-9\s\-\.\,ÁÉÍÓÚáéíóúÑñ]+$`
- **Anti-SQLi Blocklist**: Prevents inputs with `--`, `/*`, `;`, `UNION`, `SELECT`, `DROP`.
