# 🍷 Que Vino! - Stores API

Microservicio de administración de tiendas, marcas y entidades legales del ecosistema **Que Vino!**.

## 🚀 Despliegue en Producción
*   **URL Base**: `https://que-vino-stores-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app`
*   **Entorno**: Google Cloud Run (Serverless)
*   **Base de Datos**: Google BigQuery (`src_database.stores`)

## 🛠️ Herramientas para Agentes (MCP)
Este microservicio expone un servidor **Model Context Protocol (MCP)** para permitir que agentes de IA gestionen el catálogo de tiendas de forma estructurada.
*   **Herramientas**: `create_store_tool`, `update_store_tool`, `delete_store_tool`, `list_stores_tool`, `search_stores_tool`.

## 📡 Endpoints y Ejemplos (cURL)

> [!IMPORTANT]
> Todas las peticiones requieren una cabecera `Authorization: Bearer <TOKEN>` válida.

### 1. Listar Tiendas
Obtiene el catálogo completo de tiendas con paginación.
```bash
curl -X GET "https://que-vino-stores-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/stores?limit=10&offset=0" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json"
```

### 2. Buscar Tienda por Nombre
Búsqueda optimizada con normalización de caracteres.
```bash
curl -X GET "https://que-vino-stores-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/stores/search?name=Cava" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json"
```

### 3. Crear Nueva Tienda
Registro de una marca o establecimiento en el ecosistema.
```bash
curl -X POST "https://que-vino-stores-9ebf32fb-b85f-43d4-b440-af3007c90f34.a.run.app/stores" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Cava de Prova",
       "type": "Retailer",
       "is_producer": true,
       "has_wine_club": false,
       "country_code": "MX",
       "city_name": "Ensenada"
     }'
```

## 📜 Auditoría y Transaccionalidad
Todas las operaciones que modifican la base de datos son registradas automáticamente en la tabla de auditoría `src_api_transactions.stores_log` para fines de cumplimiento y rastreo.
