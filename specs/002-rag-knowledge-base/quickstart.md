# Quickstart: Gestión de Base de Conocimiento RAG (Knowledge Stores)

Este documento describe cómo poner en marcha rápidamente el microservicio de Knowledge Stores tras su implementación.

## Prerrequisitos
1. **Google Cloud SDK** autenticado con permisos de lectura en GCS (`roles/storage.objectViewer`) y permisos en BigQuery (`roles/bigquery.dataEditor`).
2. **API de Gemini habilitada** en el proyecto de Google Cloud.
3. **Credenciales de Firebase** configuradas para la validación de tokens JWT.
4. **Poetry** instalado localmente.

## Configuración del Entorno
Copia el archivo de ejemplo de variables de entorno y ajusta los valores:
```bash
cp .env.example .env
# Ajusta PROJECT_ID, BQ_DATASET, FIREBASE_PROJECT_ID, etc.
```

## Instalación y Ejecución
1. Instala las dependencias:
   ```bash
   cd apis/knowledge_stores
   poetry install
   ```
2. Inicia el servidor de desarrollo:
   ```bash
   poetry run uvicorn main:app --reload --port 8002
   ```

## Pruebas de Funcionamiento (cURL)

### 1. Sincronizar un Bucket de GCS
```bash
curl -X POST http://localhost:8002/knowledge-stores/sync \
     -H "Authorization: Bearer <TOKEN_FIREBASE>" \
     -H "Content-Type: application/json" \
     -d '{"bucket_name": "mi-bucket-de-vinos"}'
```

### 2. Listar Repositorios
```bash
curl -X GET http://localhost:8002/knowledge-stores \
     -H "Authorization: Bearer <TOKEN_FIREBASE>"
```

### 3. Eliminar un Repositorio
```bash
curl -X DELETE http://localhost:8002/knowledge-stores/mi-store-id-123 \
     -H "Authorization: Bearer <TOKEN_FIREBASE>"
```

## Logs de Auditoría
Puedes verificar la actividad de sincronización directamente en BigQuery:
```sql
SELECT * FROM `src_api_transactions.knowledge_document_sync_log`
ORDER BY event_timestamp DESC
LIMIT 50
```
