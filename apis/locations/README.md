# 📍 Que Vino! - Locations API

Microservicio de gestión de ubicaciones físicas, sucursales y geo-referenciación del ecosistema **Que Vino!**.

## 🚀 Despliegue en Producción
*   **URL Base**: `https://que-vino-locations-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app`
*   **Entorno**: Google Cloud Run (Serverless)
*   **Base de Datos**: Google BigQuery (`src_database.locations`)

## 🛠️ Herramientas para Agentes (MCP)
Este microservicio expone un servidor **Model Context Protocol (MCP)** para permitir que agentes de IA gestionen la red de sucursales de forma estructurada.
*   **Herramientas**: `create_location_tool`, `update_location_tool`, `delete_location_tool`, `list_locations_tool`, `search_locations_tool`.

## 📡 Endpoints y Ejemplos (cURL)

> [!IMPORTANT]
> Todas las peticiones requieren una cabecera `Authorization: Bearer <TOKEN>` válida.

### 1. Listar Sucursales
Obtiene todas las ubicaciones físicas registradas con paginación.
```bash
curl -X GET "https://que-vino-locations-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/locations?limit=10&offset=0" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json"
```

### 2. Buscar Sucursal
Búsqueda por ciudad o nombre de país.
```bash
curl -X GET "https://que-vino-locations-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/locations/search?term=Ensenada" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json"
```

### 3. Crear Nueva Sucursal
Registro de un punto de venta físico o establecimiento.
```bash
curl -X POST "https://que-vino-locations-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/locations" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "country_code": "MX",
       "country_name": "México",
       "state_name": "Baja California",
       "city_name": "Ensenada",
       "latitude": 31.8667,
       "longitude": -116.6167
     }'
```

## 📜 Auditoría y Transaccionalidad
Todas las operaciones que modifican la base de datos son registradas automáticamente en la tabla de auditoría `src_api_transactions.locations_log` para fines de cumplimiento y rastreo.
