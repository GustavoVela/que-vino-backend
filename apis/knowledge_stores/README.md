# 🧠 Knowledge Stores API (Que Vino!? RAG)

El micro-swarm de **Knowledge Stores** es el cerebro de indexación del ecosistema **Que Vino!?**. Este servicio orquestra la sincronización bidireccional entre **Google Cloud Storage (GCS)** y el motor de búsqueda semántica **Gemini File Search (SDK v1.70.0+ Native)**.

Su objetivo es permitir que los agentes de IA accedan a bases de conocimiento propietarias (guías de cata, manuales de sommelier, inventarios, etc.) de manera estructurada y fundamentada (Grounding).

---

## 🚀 Funcionalidades Principales

1. **Mirroring Inteligente (Sync Service)**: Sincronización incremental desde GCS hacia Gemini con control de concurrencia (Semaphore 10).
   - Detección de deltas (comparación de tamaño de archivos).
   - Limpieza automática de huérfanos (Orphan deletion).
   - Manejo de metadatos personalizados (bucket origen, tamaño exacto, fecha de carga).
2. **Gestión de Stores**: Creación, listado y eliminación de repositorios lógicos de búsqueda.
3. **Auditoría BigQuery**: Cada transacción se registra automáticamente en el dataset `src_api_transactions`.

---

## 🛠️ API REST Reference

### 1. Salud del Servicio
- **GET** `/health`
- **Respuesta**: `{"status": "ok", "environment": "dev|prod"}`

### 2. Listar Repositorios
- **GET** `/knowledge-stores`
- **Header**: `Authorization: Bearer <FIREBASE_ID_TOKEN>`
- **Descripción**: Obtiene la lista de todos los stores de Gemini activos.
- **Respuesta**:
```json
[
  { "id": "fileSearchStores/123", "display_name": "sommelier-guide-v1" },
  { "id": "fileSearchStores/456", "display_name": "inventory-logs" }
]
```

### 3. Sincronizar Base de Conocimiento (Mirroring)
- **POST** `/knowledge-stores/sync`
- **Header**: `Authorization: Bearer <FIREBASE_ID_TOKEN>`
- **Body**:
```json
{
  "bucket_name": "mi-bucket-gcs",
  "prefix": "documentacion/",
  "store_name": "Nombre Opcional del Store"
}
```
- **Parámetros**:
  - `bucket_name` (string): Requerido. Nombre del bucket de GCS origen.
  - `prefix` (string): Opcional. Filtro de subdirectorio.
  - `store_name` (string): Opcional. Si no existe, se crea un store con este nombre. Si falta, usa el nombre del bucket.
- **Respuesta (200)**:
```json
{
  "status": "completed",
  "transaction_id": "8374-2394-...",
  "summary": { "uploaded": 12, "skipped": 4, "deleted": 1, "errors": 0 }
}
```

### 4. Listar Documentos en un Store
- **GET** `/knowledge-stores/{store_id}/files`
- **Header**: `Authorization: Bearer <FIREBASE_ID_TOKEN>`
- **Parámetros Path**:
  - `store_id`: El ID corto o completo del store (ej: `123`).
- **Respuesta**: `Array<Document>`

### 5. Eliminar Store o Documento
- **DELETE** `/knowledge-stores/{store_id}`
- **DELETE** `/knowledge-stores/{store_id}/files/{file_id}`
- **Respuesta**: `204 No Content`

---

## 🔍 Métodos de Consulta (Search & Grounding)

Para ejecutar búsquedas sobre estos stores, el agente receptor (ej: Antigravity) debe:

1. **Vía Gemini Tool**: Configurar el modelo con la herramienta `file_search` apuntando al `store_id`.
   ```python
   tools = [types.Tool(file_search=types.FileSearch())]
   # Grounding query
   response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents="¿Qué dice la guía sobre el vino tinto?",
       config=types.GenerateContentConfig(tools=tools)
   )
   ```
2. **Vía MCP Tool**: Utilizar la herramienta `list_knowledge_documents` para mapear el contenido manual si no se dispone de grounding nativo.

---

## 🔒 Autenticación

El microservicio utiliza **Firebase Authentication**. Los tokens (JWT) se validan contra el proyecto configurado en `config.py`.

**Token URL**: `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[FIREBASE_API_KEY]`

---

## 📦 Desarrollo y Despliegue

```bash
# Instalación
poetry install

# Ejecución Local
python main.py

# Despliegue Cloud Run
gcloud builds submit --config deploy/cloudbuild.yaml .
```

---
© 2026 Que Vino!? - Constitución y Reglas de Agentic Architecture.
