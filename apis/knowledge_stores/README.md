# 🧠 Knowledge Stores API (Que Vino!? RAG)

El micro-swarm de **Knowledge Stores** es el cerebro de indexación del ecosistema **Que Vino!?**. Este servicio orquesta la sincronización bidireccional entre **Google Cloud Storage (GCS)** y el motor de búsqueda semántica **Gemini File Search (SDK v1.70.0+ Native)**.

Su objetivo es permitir que los agentes de IA accedan a bases de conocimiento propietarias (guías de cata, manuales de sommelier, inventarios, etc.) de manera estructurada y fundamentada (Grounding).

- **URL Producción**: `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/knowledge_stores/`
- **Resultados de Prueba**: [`tests/TEST_RESULTS.md`](tests/TEST_RESULTS.md)

---

## 🚀 Funcionalidades Principales

1. **Mirroring Inteligente (Sync Service)**: Sincronización incremental desde GCS hacia Gemini con control de concurrencia (Semaphore 10).
   - Detección de deltas (comparación de tamaño de archivos para omitir redundancias).
   - Limpieza automática de huérfanos (Orphan deletion).
   - Manejo de metadatos personalizados persistentes (bucket origen, tamaño exacto, fecha de carga).
2. **Gestión de Stores**: Creación, listado y eliminación de repositorios lógicos de búsqueda.
3. **Auditoría BigQuery**: Cada transacción se registra automáticamente en el dataset `src_api_transactions`.

---

## 🛠️ API REST Reference

Todas las peticiones (excepto `/health`) deben incluir un **Firebase ID Token** en el header `Authorization: Bearer <ID_TOKEN>`.

### 1. Salud del Servicio

**GET** `/health` *(sin autenticación)*

```bash
curl "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/health"
# → {"status": "ok", "environment": "dev"}
```

---

### 2. Listar Repositorios

**GET** `/knowledge-stores`

```bash
curl "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores" \
  -H "Authorization: Bearer <ID_TOKEN>"
```

**Respuesta (200)**:
```json
[
  { "id": "fileSearchStores/grapes-bpdsyaih31jh", "display_name": "grapes" },
  { "id": "fileSearchStores/grapesv2-g6u5ywotqjyc", "display_name": "grapes_v2" }
]
```

> [!NOTE]
> El campo `id` es el nombre completo del recurso en Gemini. El ID corto (ej: `grapes-bpdsyaih31jh`) puede usarse directamente en los endpoints de path `{store_id}`.

---

### 3. Listar Documentos en un Store
 
 **GET** `/knowledge-stores/{store_id}/files`
 
 ```bash
 # Usando el ID corto del store
 curl "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/grapes-bpdsyaih31jh/files" \
   -H "Authorization: Bearer <ID_TOKEN>"
 ```
 
 **Respuesta (200)**:
 ```json
 [
   {
     "id": "fileSearchStores/grapes-bpdsyaih31jh/documents/grapescabernet-sauvignonmd-xxx",
     "display_name": "grapes/Cabernet Sauvignon.md",
     "metadata": {
       "bucket_name": "mi-bucket-gcs",
       "original_filename": "grapes/Cabernet Sauvignon.md",
       "exact_size_bytes": "16334",
       "upload_date": "2026-04-03T23:53:38.517890"
     }
   }
 ]
 ```

---

### 4. Sincronizar Base de Conocimiento (GCS → Gemini)

**POST** `/knowledge-stores/sync`

```bash
curl -X POST "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/sync" \
  -H "Authorization: Bearer <ID_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "bucket_name": "mi-bucket-gcs",
    "prefix": "documentacion/",
    "store_name": "mi-knowledge-store"
  }'
```

| Parámetro | Tipo | Req. | Descripción |
|---|---|---|---|
| `bucket_name` | string | ✅ | Nombre del bucket de GCS origen. |
| `prefix` | string | ❌ | Filtro de subdirectorio dentro del bucket. |
| `store_name` | string | ❌ | Nombre del store destino. Si no existe, se crea. Si falta, usa el nombre del bucket. |

**Respuesta (200)**:
```json
{
  "status": "completed",
  "transaction_id": "cf99346c-85cd-48fa-bec6-6e9a7aa700d2",
  "summary": { "uploaded": 12, "skipped": 4, "deleted": 1, "errors": 0 }
}
```

---

### 5. Eliminar Store

**DELETE** `/knowledge-stores/{store_id}`  
**DELETE** `/knowledge-stores/{store_id}?force=true` *(cascade delete)*

```bash
# Intento normal (fallará si el store tiene documentos → 409)
curl -X DELETE "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/grapesv2-g6u5ywotqjyc" \
  -H "Authorization: Bearer <ID_TOKEN>"

# Cascade delete: elimina todos los documentos y luego el store
curl -X DELETE "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/grapesv2-g6u5ywotqjyc?force=true" \
  -H "Authorization: Bearer <ID_TOKEN>"
# → 204 No Content
```

| Status | Descripción |
|---|---|
| `204` | Store eliminado exitosamente. |
| `409 STORE_NOT_EMPTY` | El store contiene documentos. Usa `?force=true` o elimínalos primero. |
| `404 STORE_NOT_FOUND` | El store no existe. |

> [!NOTE]
> Gemini no permite eliminar un store que contenga documentos. Sin `?force=true`, el endpoint 
> retorna `409 Conflict` con instrucciones claras. Con `?force=true` se eliminan todos los documentos
> en cascada y luego el store.

### 6. Eliminar Documento

**DELETE** `/knowledge-stores/{store_id}/files/{file_id}`

```bash
curl -X DELETE "https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app/knowledge-stores/grapes-bpdsyaih31jh/files/grapescabernet-sauvignonmd-xxx" \
  -H "Authorization: Bearer <ID_TOKEN>"
# → 204 No Content
```

---

## 🔍 Métodos de Consulta (Search & Grounding)

Para ejecutar búsquedas sobre estos stores, el agente receptor debe:

1. **Vía Gemini Tool**: Configurar el modelo con la herramienta `file_search` apuntando al `store_id`.
   ```python
   tools = [types.Tool(file_search=types.FileSearch())]
   response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents="¿Qué dice la guía sobre el vino tinto?",
       config=types.GenerateContentConfig(tools=tools)
   )
   ```
2. **Vía MCP Tool**: Utilizar la herramienta `list_knowledge_documents` expuesta en `mcp_server.py`.

---

## 🔒 Autenticación

El microservicio utiliza **Firebase Authentication**. Los tokens (JWT) se validan contra el proyecto configurado en `config.py`.

```bash
# Obtener Firebase ID Token
curl -X POST \
  "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=<FIREBASE_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "contraseña", "returnSecureToken": true}'
```

---

## 🧪 Pruebas de Integración

Ejecutar desde la raíz del repositorio:

```bash
python3 apis/knowledge_stores/tests/test_production.py
```

Genera `apis/knowledge_stores/tests/TEST_RESULTS.md` con el detalle de todos los llamados a producción y sus respuestas.

---

## 📦 Despliegue

```bash
# Despliegue a Cloud Run (desde el root del repositorio)
gcloud builds submit \
  --config apis/knowledge_stores/deploy/cloudbuild.yaml \
  --gcs-source-staging-dir=gs://que-vino-23032025-cloudbuild/source \
  .
```

---
© 2026 Que Vino!? — Constitución v1.5.2 | Agentic Architecture.
