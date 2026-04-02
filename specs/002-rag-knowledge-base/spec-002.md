# **Feature Specification: Gestión de Base de Conocimiento RAG (Knowledge Stores)**

**Feature Branch**: 002-que-vino-rag-knowledge-base

**Created**: 2026-03-30

**Status**: Draft (Iteración 3 - Simplificación Auth y Sync por Bucket)

**Target Persona (Primary)**: Administrador de Datos / Data Engineer.

**Target Persona (Secondary)**: Desarrollador Backend / Agentes IA.

## **Executive Context & Market Opportunity *(mandatory)***

**Problem Statement:** Para que la Inteligencia Artificial de "Que Vino" (basada en Gemini) pueda ofrecer recomendaciones precisas, notas de cata exactas y responder dudas sobre catálogos de proveedores, el modelo requiere contexto externo mediante Generación Aumentada por Recuperación (RAG). Gestionar la ingesta de estos documentos manualmente en la consola de Google es ineficiente y no auditable. Además, para evitar colisiones lógicas con nuestras tiendas físicas (Stores), necesitamos una API segura e incremental para gestionar **"Knowledge Stores"** (Repositorios de Conocimiento).

En esta iteración, adoptamos **Google Cloud Storage (GCS)** como nuestra fuente única de la verdad documental. La API utilizará la herramienta *File Search* de Gemini para sincronizar inteligentemente los repositorios leyendo directamente de los buckets de GCS. Se utilizará el **nombre del bucket** como el identificador y nombre del repositorio. La API optimizará costos listando el contenido de ambos lados (GCS y Gemini) para sincronizar únicamente archivos nuevos, re-indexar aquellos que han cambiado de tamaño, y eliminar de la IA los que ya no existen en el bucket, asegurando que la "memoria" del LLM sea siempre un espejo exacto y confiable de nuestra nube.

**Out of Scope (Non-Goals):** * **Definición e implementación de Roles y Permisos granulares (RBAC)**. Todo usuario con sesión válida en Firebase tiene acceso.

* Creación de una interfaz gráfica de usuario (Frontend) para la carga masiva de archivos.  
* Endpoint de inferencia o chat del LLM (este documento cubre estrictamente la *ingesta* y *gestión* del conocimiento).  
* Implementación de esquemas de funciones / herramientas MCP en este componente (la API operará de forma independiente).  
* Gestión del inventario en tiempo real (eso corresponde a otras APIs).

## **User Scenarios & Testing *(mandatory)***

### **User Story 1 - Autenticación, Acceso a APIs y Sincronización de Usuarios (Priority: P0)**

Como sistema de seguridad central, quiero requerir autenticación mediante Google/Firebase para cualquier solicitud a la API, verificando la validez del token y almacenando/actualizando el perfil del usuario para asegurar la trazabilidad absoluta (quién hace qué) antes de permitir la interacción con Gemini, en estricta alineación con el PRD-001.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Sincronización de Perfil**: Dado un token JWT válido enviado por primera vez o con datos actualizados, cuando el backend lo recibe, entonces decodifica el payload (nombre, foto, email) y realiza un Upsert (Insert/Update) en la tabla src_database.users para mantener el registro interno del usuario. De forma asíncrona, registra un evento SUCCESS en src_api_transactions.authentication_log.  
2. **Autenticación Exitosa**: Dado un request a la API con un header Authorization: Bearer <token> válido, entonces el backend procesa la petición correctamente y registra asíncronamente el intento exitoso en src_api_transactions.authentication_log.  
3. **Token Ausente**: Dado un request a un endpoint protegido (GET, POST, DELETE), cuando el header Authorization no existe, entonces la API responde con **401 Unauthorized** inmediatamente y registra de forma asíncrona un evento FAILED sin user_id.  
4. **Token Expirado o Inválido**: Dado un request con un token manipulado o caducado, cuando el backend lo valida, rechaza la petición con **401 Unauthorized** y registra asíncronamente un evento FAILED con el detalle en el log de autenticación.

### **User Story 2 - Ingesta y Sincronización Incremental por Bucket (Priority: P1)**

Como Data Engineer, quiero ejecutar un endpoint enviando el bucket_name de Google Cloud Storage para que el sistema sincronice su contenido hacia un Knowledge Store de Gemini. El proceso interno debe listar ambos orígenes y decidir qué acciones tomar (crear, actualizar o borrar) reflejando el estado actual del bucket.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Ingesta de Archivo Nuevo**: Dado un archivo en GCS que no existe en el Knowledge Store de Gemini, cuando se envía un POST /knowledge-stores/sync con el body {"bucket_name": "que-vino-23032025-databases/grapes"}, entonces la API lee el archivo de GCS, lo sube a Gemini, inyecta su metadata (size_bytes, original_filename), y registra un log UPLOADED en knowledge_document_sync_log.  
2. **Sincronización Incremental (Skip)**: Dado un archivo que existe tanto en el bucket de GCS como en Gemini, cuando tienen *exactamente el mismo tamaño en bytes*, entonces el archivo se omite, no se consume API de Google, y se registra un log SKIPPED.  
3. **Actualización por Diferencia de Tamaño**: Dado un archivo que existe en ambos lados, cuando el peso en bytes en GCS difiere del reportado en la metadata de Gemini, entonces la API borra la versión antigua en Gemini, sube la nueva versión, y registra un log REPLACED o UPLOADED.  
4. **Limpieza de Huérfanos (Borrado Automático)**: Dado un archivo indexado en Gemini que *ya no existe* en el bucket respectivo de GCS (basado en el listado comparativo), cuando se ejecuta el sync, entonces la API elimina proactivamente el archivo de Gemini y registra un log DELETED_ORPHAN.

### **User Story 3 - Listado Total de Repositorios y Archivos (Priority: P1)**

Como Administrador o Agente IA, quiero consultar todos los repositorios disponibles en Gemini y extraer la lista completa de archivos de un repositorio específico, sin lidiar con paginación, para facilitar el contexto.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Listado de Repositorios Activos**: Dado un usuario autenticado, cuando solicita GET /knowledge-stores, entonces el sistema consulta Gemini para obtener la lista de todos los repositorios disponibles, registra el evento SELECT asíncronamente en knowledge_store_api_log, y responde con **200 OK** y la lista completa.  
2. **Listado Completo de Archivos**: Dado un ID de repositorio válido, cuando solicito GET /knowledge-stores/{id}/files, entonces la API extrae iterativamente **todos** los archivos internamente desde Gemini y responde con **200 OK** devolviendo un arreglo JSON plano con la totalidad de los documentos y su metadata, sin paginación para el cliente.  
3. **Repositorio No Encontrado**: Dado un ID que no existe, cuando se consulta, entonces la API responde con **404 Not Found**.

### **User Story 4 - Depuración de Conocimiento (Borrado Manual) (Priority: P2)**

Como Administrador de Datos, quiero eliminar repositorios completos o forzar el borrado de archivos específicos directamente en Gemini si es necesario por una emergencia de datos.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Borrado de Archivo Único**: Dado un usuario autenticado, cuando envía DELETE /knowledge-stores/{store_id}/files/{file_id}, entonces la API elimina permanentemente el archivo en Gemini (sin tocar GCS), graba el evento en knowledge_document_sync_log y devuelve **204 No Content**.  
2. **Borrado de Repositorio Completo**: Dado un usuario autenticado, cuando envía DELETE /knowledge-stores/{store_id}, entonces la API borra el contenedor en Gemini, remueve el mapeo interno asociado al bucket, registra un log DELETE_STORE y devuelve **204 No Content**.

## **Edge Cases & Exception Handling**

* **Errores de Permisos en Cloud Storage (HTTP 403)**: Si la API no tiene permisos IAM para leer el bucket_name especificado, el proceso de sincronización debe abortar inmediatamente devolviendo un HTTP 500 al cliente y registrando un log de error crítico.  
* **Rate Limiting (Gemini API 429)**: Si durante una ingesta masiva la API de Gemini devuelve un HTTP 429, el sistema implementará *Exponential Backoff*. Tras 5 reintentos fallidos, el archivo se marca como ERROR_NETWORK en el log de BQ y la sincronización avanza.  
* **Fallo de Base de Datos (Timeouts en Auditoría)**: Si BigQuery no responde, al ser el registro de logs asíncrono, la transacción principal hacia Gemini *debe continuar*, guardando el log fallido en una cola de mensajes en memoria.  
* **Archivos No Soportados**: Si en GCS hay un .exe o formato no aceptado por Gemini, la API omitirá el archivo, lo marcará como ERROR_UNSUPPORTED en el log, y continuará.

## **Business Rules & API Contracts**

### **Contrato de Autenticación y Auditoría Híbrida**

* **Delegación de Identidad Universal**: El sistema confía plenamente en el token JWT emitido por Firebase. Ninguna operación de lectura o escritura puede procesarse sin extraer previamente el user_id y sincronizarlo contra la tabla src_database.users.  
* **Auditoría Estrictamente Asíncrona (Performance Protection)**: Las inserciones hacia src_api_transactions.knowledge_document_sync_log y src_api_transactions.authentication_log deben delegarse obligatoriamente a tareas en segundo plano (BackgroundTasks) para no penalizar el tiempo de respuesta HTTP.

### **Contrato de Sincronización "Mirroring" con GCS**

* **GCS es Solo Lectura (Read-Only)**: La API *NUNCA* escribirá, modificará ni borrará archivos dentro de Google Cloud Storage. Su único rol respecto a GCS es descargar el flujo de bytes para enviarlo a Gemini.  
* **Inyección Obligatoria de Metadata**: Todo archivo subido exitosamente a Gemini *debe* llevar inyectado:  
  * bucket_name (string): Nombre del origen en GCS.  
  * original_filename (string): Nombre real del archivo en GCS.  
  * exact_size_bytes (string/int): Tamaño exacto del objeto extraído de GCS metadata.  
  * upload_date (ISO 8601).  
* **Lógica Comparativa Interna**: El endpoint /knowledge-stores/sync ejecuta la evaluación sin depender del cliente:  
  1. Lista todos los blobs disponibles en bucket_name (GCS).  
  2. Lista todos los archivos del repositorio correspondiente en Gemini.  
  3. Ejecuta operaciones Delta comparando por nombre y exact_size_bytes.

## **Key Entities & BigQuery Schema (Data Structures)**

### **1. Tabla: src_database.users (Usuarios Autenticados)**

*Estructura alineada milimétricamente con PRD-001 (Sin roles/privilegios).*

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | PRIMARY KEY | UID de Firebase. |
| email | STRING | REQUIRED | Correo electrónico principal del usuario. |
| email_verified | BOOLEAN | REQUIRED | Indica si el correo ha sido verificado. |
| display_name | STRING | REQUIRED | Nombre a mostrar del usuario. |
| photo_url | STRING | NULLABLE | URL de la foto de perfil. |
| phone_number | STRING | NULLABLE | Número de teléfono asociado. |
| provider_id | STRING | NULLABLE | Proveedor de identidad. |
| created_at | TIMESTAMP | REQUIRED | Momento de creación. |
| updated_at | TIMESTAMP | REQUIRED | Última vez que el usuario inició sesión o actualizó su token. |

**Configuración de Optimización (BigQuery):**

* **Particionamiento:** created_at (por día)  
* **Clusterización:** provider_id, email_verified

### **2. Tabla: src_api_transactions.authentication_log**

*Log append-only de accesos (Alineado con PRD-001).*

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware. |
| user_id | STRING | NULLABLE | Firebase UID. |
| email | STRING | REQUIRED | Correo de intento. |
| status | STRING | REQUIRED | SUCCESS, FAILED. |
| error_message | STRING | NULLABLE | Detalle de fallo de JWT. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento de ejecución (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BQ. |

**Configuración de Optimización (BigQuery):**

* **Particionamiento:** event_timestamp (por día)  
* **Clusterización:** status, email, user_id

### **3. Tabla: src_api_transactions.knowledge_store_api_log (Gestión de Repositorios)**

*Audita acciones a nivel de contenedor.*

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado en el request HTTP. |
| bucket_name | STRING | REQUIRED | Nombre del bucket/repositorio de GCS (ej. 'que-vino-databases/mx'). |
| store_id_gemini | STRING | NULLABLE | ID real alfanumérico devuelto por Google. |
| performed_by_user_id | STRING | REQUIRED | UID de Firebase del ejecutor. |
| transaction_api_type | STRING | REQUIRED | 'GET', 'POST', 'DELETE'. |
| transaction_db_type | STRING | REQUIRED | 'CREATE_STORE', 'DELETE_STORE', 'LIST_STORES'. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento de la petición. |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BQ. |

**Configuración de Optimización (BigQuery):**

* **Particionamiento:** event_timestamp (por día)  
* **Clusterización:** transaction_api_type, transaction_db_type, bucket_name

### **4. Tabla: src_api_transactions.knowledge_document_sync_log (Sincronización de Archivos)**

*Registro granular para conciliar la facturación de embeddings de Google.*

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | Trace ID de la petición padre. |
| bucket_name | STRING | REQUIRED | Identificador del repositorio/bucket origen. |
| store_id_gemini | STRING | REQUIRED | ID en Google GenAI. |
| file_name | STRING | REQUIRED | Nombre original del documento en GCS. |
| action_taken | STRING | REQUIRED | 'UPLOADED', 'SKIPPED', 'DELETED_FILE', 'DELETED_ORPHAN', 'ERROR_NETWORK', 'ERROR_UNSUPPORTED'. |
| file_size_bytes | INT64 | NULLABLE | Peso exacto del archivo en bytes (desde GCS). |
| performed_by_user_id | STRING | REQUIRED | UID de Firebase del ejecutor. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de evaluación/carga. |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BQ. |

**Configuración de Optimización (BigQuery):**

* **Particionamiento:** event_timestamp (por día)  
* **Clusterización:** action_taken, bucket_name, store_id_gemini

## **Success Criteria *(mandatory)***

### **Layer 1: Measurable Outcomes (Business Result)**

* **SC-001 (Zero-Touch Mirroring)**: El sistema permite reflejar con exactitud el contenido de un bucket de GCS hacia un Gemini Knowledge Store iterando e igualando ambas listas automáticamente.  
* **SC-002 (Security Compliance)**: 100% de las operaciones de mutación validan un token JWT de Firebase y registran el user_id en las tablas de auditoría asíncrona (alineado al PRD-001).

### **Layer 2: API Performance & Integration**

* **Target Latency**: Los endpoints de listado (GET /knowledge-stores) deben responder rápidamente. La latencia del endpoint de sincronización o de archivos totales dependerá de la red, pero se manejarán transparentemente para el cliente sin paginación tediosa.  
* **Cost Efficiency**: Demostrar mediante logs que ejecuciones consecutivas del endpoint de sincronización sobre un bucket de GCS sin alteraciones arrojan un 100% de action_taken = 'SKIPPED'.

### **Layer 3 & 4: Data Quality and Operational Readiness**

* **Data Quality (Metadata)**: 100% de los archivos cargados poseen inyectados los campos exact_size_bytes y bucket_name en Gemini.  
* **Audit Integrity**: La sumatoria de eventos de sincronización en knowledge_document_sync_log debe conciliar el inventario reportado por la consola de Google Cloud para Gemini.