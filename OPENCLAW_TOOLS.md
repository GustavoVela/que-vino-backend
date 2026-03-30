# Que Vino OPENCLAW API Inventory

This document tracks all productive APIs and agents exposed in the `que-vino-backend` ecosystem for cross-reference.

## APIs

### 1. Stores API
- **Repository Path**: `apis/stores/`
- **MCP Server Path**: `apis/stores/mcp_server.py`
- **Security**: Requires Firebase Bearer Tokens

#### 1.1 List Stores
- **Method / Path**: `GET /stores`
- **URL Parameters**: `limit=100`, `offset=0`
- **Required Headers**: `Authorization: Bearer <ID_TOKEN>`
- **Response**: Array of Store details.
```json
[
  {
    "id": "uuid-v4",
    "name": "Vinoteca Nacional",
    "type": "Retail",
    "country_code": "MX",
    "country_name": "México",
...
```

#### 1.2 Create Store
- **Method / Path**: `POST /stores`
- **Required Headers**: `Authorization: Bearer <ID_TOKEN>`
- **Request Body** (`StoreCreate`):
```json
{
  "name": "Cava de Vinos",
  "type": "Tienda Especializada",
  "digital_platform": "Shopify",
  "is_producer": false,
  "has_wine_club": true,
  "representative_name": "Juan Perez",
  "country_code": "MX",
  "country_name": "México",
  "state_code": "CDMX",
  "state_name": "Ciudad de México",
  "city_code": "MEX",
  "city_name": "Ciudad de México",
  "address": "Av. Reforma 123",
  "contact_email": "hola@cavadevinos.com",
  "contact_phone": "+525512345678",
  "website_url": "https://cavadevinos.com",
  "social_media": {"instagram": "@cava_vinos"},
  "description": "Tienda especialista en vinos naturales"
}
```
- **Response** `201 Created`: The created store object including `id`, `created_at`, `updated_at`.

#### 1.3 Search Stores
- **Method / Path**: `GET /stores/search`
- **URL Parameters**: `city_code` (str), `country_code` (str), `limit=100`, `offset=0`
- **Response**: Filtered Array of Store objects.


---

### 2. Locations API
- **Repository Path**: `apis/locations/`
- **MCP Server Path**: `apis/locations/mcp_server.py`
- **Security**: Requires Firebase Bearer Tokens

#### 2.1 List Locations
- **Method / Path**: `GET /locations`
- **URL Parameters**: `limit=100`, `offset=0`
- **Required Headers**: `Authorization: Bearer <ID_TOKEN>`
- **Response**:
```json
[
  {
    "id": "uuid-v4",
    "country_code": "CO",
    "country_name": "Colombia",
    "state_code": "DC",
    "state_name": "Bogotá D.C.",
    "city_code": "BOG",
    "city_name": "Bogotá",
    "latitude": 4.6533817,
    "longitude": -74.0836331,
    "created_at": "2026-03-29T10:00:00Z",
    "updated_at": "2026-03-29T10:00:00Z"
  }
]
```

#### 2.2 Create Location
- **Method / Path**: `POST /locations`
- **Required Headers**: `Authorization: Bearer <ID_TOKEN>`
- **Request Body** (`LocationCreate`):
```json
{
  "country_code": "FR",
  "country_name": "France",
  "state_code": "BCA",
  "state_name": "Bordeaux",
  "city_code": "BX",
  "city_name": "Bordeaux",
  "latitude": 44.837789,
  "longitude": -0.57918
}
```
- **Response** `201 Created`: The created location object including automatic `id`, `created_at`.

#### 2.3 Search Locations
- **Method / Path**: `GET /locations/search`
- **URL Parameters**: `country_code` (str), `state_code` (str), `limit=100`, `offset=0`
- **Response**: Array of locations that match exact filters.

#### 2.4 Delete Locations
- **Method / Path**: `DELETE /locations/{id}`
- **Required Headers**: `Authorization: Bearer <ID_TOKEN>`
- **Response**: `{ "detail": "Location deleted successfully" }`
