# Que Vino! Knowledge Stores API

Esta API es el motor de conocimiento (RAG) del proyecto **Que Vino!**. Utiliza el SDK nativo de **Gemini GenAI (v1.70.0+)** para indexar documentos desde Google Cloud Storage hacia los *File Search Stores* de Gemini, permitiendo que los agentes inteligentes realicen búsquedas semánticas precisas sobre el catálogo, guías de sommelier y otros documentos de soporte.

## 🚀 Despliegue en Producción
**URL Base:** `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`

## 🛠️ Herramientas para Agentes (MCP)
Esta API expone un servidor MCP que permite a los agentes de IA:
1. `sync_bucket`: Sincronizar un bucket de GCS con Gemini.
2. `list_knowledge_stores`: Listar los repositorios de conocimiento disponibles.
3. `query_knowledge`: (Próximamente) Realizar búsquedas directamente en los stores.

## 📝 Ejemplos de uso con cURL

> [!WARNING]
> El token proporcionado es de **prueba y expira**. Reemplaza `<TU_TOKEN>` con un token válido generado mediante `gcloud auth print-access-token` o un Firebase ID Token.

### 1. Salud del Servicio (Health Check)
```bash
curl -X GET "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/health"
```

### 2. Listar Repositorios de Gemini (Stores)
```bash
curl -X GET "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/stores" \
     -H "Authorization: Bearer [GCLOUD_TOKEN_HERE]"
```

### 3. Sincronizar un Bucket de GCS
Sincroniza el contenido de un bucket hacia un store de Gemini. Si el store no existe, se crea automáticamente.
```bash
curl -X POST "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/sync-bucket" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer [GCLOUD_TOKEN_HERE]" \
     -d '{
       "bucket_name": "que-vino-knowledge-base",
       "store_name": "sommelier_knowledge",
       "user_id": "test-admin"
     }'
```

### 4. Listar Documentos en un Store
```bash
curl -X GET "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/stores/fileSearchStores/TU_STORE_ID/documents" \
     -H "Authorization: Bearer [GCLOUD_TOKEN_HERE]"
```

## 🏗️ Arquitectura
* **Backend:** FastAPI (Python 3.12+).
* **IA:** Gemini Native SDK (v1.70.0+).
* **Logs:** Registro de eventos asíncronos en BigQuery (`que_vino_transactions`).
* **Concurrencia:** Sincronización masiva paralela mediante semáforos de `asyncio`.
