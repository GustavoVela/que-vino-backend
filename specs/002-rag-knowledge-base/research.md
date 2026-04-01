# Research: Gestión de Base de Conocimiento RAG (Knowledge Stores)

Este documento detalla las decisiones técnicas y hallazgos tras la investigación de las APIs de Google Generative AI y Google Cloud Storage para la implementación del sistema de Knowledge Stores.

## Decisiones Técnicas

### 1. SDK de Gemini para RAG
- **Decisión**: Utilizar el módulo `file_search_stores` del SDK `google-generativeai`.
- **Rationale**: A diferencia de la `Files API` (que es temporal por 48 horas), las `File Search Stores` son persistentes y están diseñadas específicamente para RAG y búsqueda semántica de largo plazo.
- **Métodos Clave**:
    - `client.file_search_stores.list()`: Para listar todos los repositorios.
    - `client.file_search_stores.list_documents(name=store_name)`: Para listar documentos en un store específico.
    - `client.file_search_stores.delete_document(name=doc_name)`: Para eliminar documentos huérfanos.

### 2. Sincronización Incremental (Mirroring)
- **Decisión**: Implementar un algoritmo de comparación de inventarios entre GCS y Gemini basado en `file_name` y `exact_size_bytes`.
- **Lógica**:
    1. Obtener lista de blobs de GCS (`blob.name`, `blob.size`).
    2. Obtener lista de documentos de Gemini con su metadata inyectable.
    3. **Subir**: Archivos en GCS que no existen en Gemini.
    4. **Actualizar**: Archivos cuyo tamaño en bytes en GCS difiere del registrado en Gemini (Borrar + Subir).
    5. **Omitir**: Archivos con mismo nombre y tamaño (Status `SKIPPED`).
    6. **Borrar**: Archivos en Gemini que ya no existen en el bucket de GCS (`DELETED_ORPHAN`).

### 3. Auditoría Asíncrona (BigQuery)
- **Decisión**: Usar `BackgroundTasks` de FastAPI para las inserciones en BigQuery.
- **Rationale**: Evita que la latencia de red de BigQuery penalice el tiempo de respuesta de la API, especialmente en el endpoint de sincronización que puede procesar muchos archivos.
- **Manejo de Errores**: Si falla la inserción en BQ, se registrará en el log estándar del servidor (stderr) para no interrumpir la lógica de negocio principal pero permitir su diagnóstico.

### 4. Mapeo Bucket -> Store
- **Decisión**: Usar el `bucket_name` como el `display_name` del Store en Gemini para mantener una relación 1:1 clara.
- **Almacenamiento**: No se requiere una tabla de mapeo persistente en BigQuery ya que la relación se puede derivar dinámicamente listando los stores en Gemini y comparando con los buckets autorizados.

## Alternativas Consideradas
- **Almacenar estado en BigQuery**: Se descartó para evitar inconsistencias entre la DB y la realidad de Gemini. La "fuente de la verdad" siempre será el listado en vivo de ambos servicios.
- **Files API de Gemini**: Descartada por su naturaleza temporal (expiración de 48 horas), lo cual es incompatible con una base de conocimiento persistente.

## Referencias
- [Google Generative AI Python SDK Documentation](https://ai.google.dev/api/python/google/generativeai)
- [Google Cloud Storage Python Client](https://cloud.google.com/storage/docs/reference/libraries#python)
