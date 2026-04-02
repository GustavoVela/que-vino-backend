# **Feature Specification: Gestión de Tiendas y Localizaciones (CRUD, APIs y MCP)**

**Feature Branch**: 001-que-vino-auth-stores-y-locations
**Created**: 2026-03-26
**Status**: Draft (Iteración 8 - Cobertura Total de APIs en MCP)
**Target Persona (Primary)**: Administrador de Datos / Content Manager.
**Target Persona (Secondary)**: Desarrollador Backend / Agentes IA (MCP) / Ingeniero de Datos.

## **Executive Context & Market Opportunity *(mandatory)***

**Problem Statement:** Para que "Que Vino" se convierta en la plataforma de referencia, necesitamos estructurar la información dispersa de las tiendas de vino y sus localizaciones. Carecemos de un sistema protegido, estandarizado y consultable. Necesitamos una base de datos escalable en BigQuery mediante APIs RESTful que soporten operaciones de creación y actualización continua, búsquedas avanzadas y paginadas (tolerantes a errores tipográficos y acentos), y que expongan estas capacidades a modelos de Inteligencia Artificial (MCP) de forma extremadamente segura.

**Out of Scope (Non-Goals):** * Definición e implementación de Roles y Permisos granulares (RBAC). Todo usuario con sesión válida en Firebase tiene acceso.

* Gestión de inventario de botellas o SKUs por tienda.  
* Pasarelas de pago o transacciones de e-commerce directas.  
* Registro de usuarios finales/consumidores.

## **User Scenarios & Testing *(mandatory)***

### **User Story 1 - Autenticación, Acceso a APIs y Sincronización de Usuarios (Priority: P0)**

Como Administrador, quiero autenticarme en la plataforma utilizando Google OAuth para obtener un token de acceso y que el sistema registre mi perfil en la base de datos interna, permitiéndome interactuar de forma segura y trazable con las APIs de gestión.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Sincronización de Perfil**: Dado un token JWT válido enviado por primera vez o con datos actualizados, cuando el backend lo recibe, entonces decodifica el payload (nombre, foto, email) y realiza un Upsert (Insert/Update) en la tabla src_database.users para mantener el registro interno del usuario. De forma asíncrona (en segundo plano), registra un evento `SUCCESS` en la tabla `src_api_transactions.authentication_log`.
2. **Autenticación Exitosa**: Dado un cliente web que completa el flujo de Google, cuando envía una petición a la API con un header Authorization: Bearer <token> válido, entonces el backend procesa la petición correctamente y registra asíncronamente el intento exitoso en `src_api_transactions.authentication_log`.
3. **Token Ausente**: Dado un request a un endpoint protegido (GET, POST, PUT, DELETE), cuando el header Authorization no existe, entonces la API responde con **401 Unauthorized** inmediatamente. De manera asíncrona, registra un evento `FAILED` en `src_api_transactions.authentication_log` (sin `user_id`).
4. **Token Expirado o Inválido**: Dado un request con un token manipulado o caducado, cuando el backend lo valida contra Firebase, entonces rechaza la petición con **401 Unauthorized** y el body `{"error": "Token expired or invalid"}`. Simultáneamente, registra de forma asíncrona un evento `FAILED` con el detalle del error en `src_api_transactions.authentication_log`.

### **User Story 2 - Ingesta y Actualización de Tiendas (CRUD Seguro) (Priority: P1)**

Como Administrador de Datos, quiero crear nuevas tiendas y actualizar la información de las tiendas existentes basándome en su ID único, para mantener el catálogo siempre al día.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Creación Exitosa (Create)**: Dado un payload JSON válido sin ID, cuando se envía un POST /stores, entonces el sistema genera un UUID4, persiste el registro en `src_database.stores`, crea el log de tipo `INSERT` de manera **síncrona** en `src_api_transactions.stores_log`, y responde con **201 Created** y el objeto creado.  
2. **Actualización Exitosa (Update)**: Dado un registro existente con ID 1234-abcd, cuando se envía un PUT /stores/1234-abcd con datos modificados, entonces el sistema actualiza únicamente ese registro en `src_database.stores`, guarda el estado previo y nuevo de forma **síncrona** en `src_api_transactions.stores_log` con tipo `UPDATE`, y responde con **200 OK**.  
3. **Actualización Inexistente**: Dado un ID que no está en la base de datos, cuando se intenta un PUT /stores/{id}, entonces la API responde con **404 Not Found** y el mensaje {"error": "Store not found"}.  
4. **Errores de Validación**: Dado un intento de crear o actualizar, cuando se omiten campos obligatorios (ej. name), o se envían tipos de datos incorrectos, entonces la API responde con **422 Unprocessable Entity** detallando los campos erróneos.  
5. **Conflictos**: Dado un intento de registrar un correo de contacto o URL que ya existe para otra tienda (si se define como único en reglas de negocio posteriores), cuando se envía el request, entonces la API responde con **409 Conflict**.

### **User Story 3 - Listado, Búsqueda Avanzada y Paginación (Priority: P1)**

Como usuario o Agente IA, quiero listar el catálogo completo o buscar tiendas usando una combinación flexible de parámetros (nombre, ciudad, estado, país) y navegar por los resultados de forma paginada.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Listado General Paginado**: Dado un catálogo de 500 tiendas, cuando solicito GET /stores?page=1&limit=20, entonces el sistema registra un evento `SELECT` con los parámetros y filtros de consulta de forma **síncrona** en `src_api_transactions.stores_log`, y responde con **200 OK**, devolviendo las primeras 20 tiendas y los metadatos de paginación {"data": [...], "meta": {"total_items": 500, "total_pages": 25, "current_page": 1, "limit": 20}}.  
2. **Búsqueda Múltiple y Normalizada**: Dado que existen las tiendas "El rincón del Vino" (CDMX) y "Vinos México" (Jalisco), cuando busco GET /stores/search?name=Rincon&city=cdmx, entonces el sistema normaliza el texto (quita acentos, pasa a minúsculas), documenta el evento `SELECT` de manera **síncrona** en `src_api_transactions.stores_log`, y devuelve "El rincón del Vino" con **200 OK**.  
3. **Búsqueda sin Resultados**: Dado un criterio que no coincide con nada, cuando ejecuto la búsqueda, entonces el sistema almacena el intento de lectura de forma **síncrona** en `src_api_transactions.stores_log` y devuelve **200 OK** con una lista vacía [] y total_items: 0 (no un error 404).

### **User Story 4 - Gestión del Catálogo de Localizaciones (Priority: P2)**

Como Administrador de Datos, quiero listar, crear y actualizar un catálogo (CRUD) de ubicaciones para estandarizar los filtros de búsqueda.

**Acceptance Scenarios (API Behavior & HTTP Codes):**

1. **Listado de Localizaciones**: Dado un front-end que necesita poblar un selector, cuando solicita GET /locations?page=1&limit=50, entonces el sistema guarda el registro de la consulta `SELECT` de manera **síncrona** en `src_api_transactions.locations_log` y devuelve la lista paginada de ubicaciones con **200 OK**.  
2. **Update de Localización**: Dado un registro de localización existente, cuando envío un PUT /locations/{id} para corregir el nombre de una ciudad, entonces el sistema actualiza el registro en `src_database.locations`, graba el `UPDATE` con el log *before/after* de forma **síncrona** en `src_api_transactions.locations_log`, y responde con **200 OK**.  
3. **Validación de Integridad**: Dado un intento de POST /locations, cuando el country_code tiene más de 2 caracteres (ej. MEX), entonces el sistema bloquea la acción con **422 Unprocessable Entity**.

## **Edge Cases & Exception Handling**

* **Rate Limiting (Abuso de APIs)**: Si una IP o un token realiza más de 100 peticiones por minuto, la API debe bloquear temporalmente las solicitudes retornando **429 Too Many Requests**.  
* **Fallo de Base de Datos (Timeouts)**: Si BigQuery o la base transaccional no responde en menos de 5 segundos, la API debe abortar la operación limpiamente retornando **500 Internal Server Error** sin exponer stack traces al cliente.  
* **Concurrent Updates (Condición de Carrera)**: Si dos administradores intentan actualizar la misma tienda (PUT) exactamente al mismo tiempo, el sistema procesará secuencialmente asegurando que la tabla audit_log capture ambos eventos con timestamps distintos.

## **Business Rules & API Contracts**

### **Contrato de Autenticación y Auditoría**

* **Delegación de Identidad**: El sistema confía plenamente en el token JWT emitido por Firebase. Ninguna operación de lectura (GET) y escritura (POST, PUT, DELETE) puede procesarse sin extraer previamente el user_id y sincronizarlo contra la tabla src_database.users.  
* **Inmutabilidad de Registros Críticos (Operaciones sobre Tiendas y Localizaciones)**: Toda operación realizada a través de la API de Stores y Locations (sean validaciones de escritura mediante POST, PUT, DELETE, o consultas de lectura como SELECT) deberá generar un `transaction_id` único y escribirse de manera estrictamente **síncrona** en su tabla log correspondiente (`src_api_transactions.stores_log` o `src_api_transactions.locations_log`). La petición al cliente no devolverá su *response* hasta que la inserción dentro de BigQuery se ejecute con éxito protegiendo la trazabilidad exacta de los datos.
* **Operaciones de Logging Asíncronas (Autenticación Exclusiva)**: Al contrario del requerimiento estricto para los catálogos, todo intento de autenticación y acceso general al sistema continuará rastreándose de manera obligatoria en la tabla `src_api_transactions.authentication_log` manejada **en segundo plano asíncronamente** (a través de `BackgroundTasks` de FastAPI), garantizando que las funciones de autenticación eviten degradación del performance percibido en la página de inicio.

### **Contrato de Normalización y Paginación**

* **Motor de Búsqueda Flexible**: Los endpoints GET /search procesan los parámetros como opcionales e inclusivos (condiciones AND si se envían varios).  
* **Sanitización y Normalización**: Antes de consultar la base de datos, todo texto de entrada debe ser despojado de tildes/acentos y convertido a minúsculas (UNACCENT(LOWER(termino))).  
* **Paginación Obligatoria Universal**: Todo endpoint GET (/stores, /locations, /stores/search) debe implementar por defecto page=1 y limit=20 si el cliente no los especifica, limitando el máximo a limit=100 para proteger la memoria del servidor. La respuesta **siempre** debe incluir el bloque "meta" con los detalles de paginación.

## **Integración Model Context Protocol (MCP) & Safeguards**

Para que la IA interactúe con el catálogo de forma exhaustiva, el servidor MCP expondrá **todas las operaciones del CRUD** como herramientas, permitiendo no solo la consulta sino la gestión delegada del catálogo.

### **Herramientas MCP para Tiendas (Stores API)**

1. **list_stores**: Obtiene el catálogo de tiendas paginado.  
   * **Input**: { "page": "number (opcional)", "limit": "number (opcional)" }  
2. **search_stores**: Busca tiendas usando criterios flexibles y normalizados.  
   * **Input**: { "name": "string (opcional)", "city": "string (opcional)", "state": "string (opcional)", "country": "string (opcional)" }  
3. **create_store**: Crea un nuevo registro de tienda en el sistema.  
   * **Input**: { "name": "string (requerido)", "is_producer": "boolean (requerido)", "country": "string (requerido)", "city": "string (requerido)", "has_wine_club": "boolean (requerido)", ...otros_campos_opcionales }  
4. **update_store**: Modifica una tienda existente mediante su ID.  
   * **Input**: { "id": "string UUID (requerido)", "name": "string (opcional)", "city": "string (opcional)", ...otros_campos_opcionales }  
5. **delete_store**: Elimina una tienda existente mediante su ID.  
   * **Input**: { "id": "string UUID (requerido)" }

### **Herramientas MCP para Localizaciones (Locations API)**

1. **list_locations**: Obtiene el catálogo de ubicaciones paginado.  
   * **Input**: { "page": "number (opcional)", "limit": "number (opcional)" }  
2. **search_locations**: Busca ubicaciones específicas.  
   * **Input**: { "city": "string (opcional)", "state": "string (opcional)", "country_code": "string (opcional)" }  
3. **create_location**: Añade una nueva ubicación al catálogo.  
   * **Input**: { "country_code": "string (requerido)", "country_name": "string (requerido)", "city": "string (requerido)", "city_code": "string (requerido)", "state": "string (opcional)" }  
4. **update_location**: Modifica una ubicación existente.  
   * **Input**: { "id": "string UUID (requerido)", "city": "string (opcional)", "state": "string (opcional)", ... }  
5. **delete_location**: Elimina una ubicación del catálogo.  
   * **Input**: { "id": "string UUID (requerido)" }

### **MCP Security Guardrails (Protección Anti-Prompt Injection & Operacional)**

Dado que los parámetros provienen de un LLM (que puede ser manipulado por el usuario), las herramientas MCP **deben implementar validaciones estrictas** antes de enviar la petición a la API de Que Vino:

1. **Delegación de Autenticación**: El servidor MCP no elude la seguridad. Para ejecutar herramientas de mutación (create_*, update_*, delete_*), el servidor MCP debe recibir e inyectar el token JWT del usuario que está interactuando con el LLM en ese momento. Si no hay token, la herramienta MCP debe fallar proactivamente.  
2. **Restricción de Longitud**: Ningún parámetro de búsqueda o campo de texto corto recibido en el MCP puede exceder los 50 caracteres (excepto URLs o descripciones que tienen su propio límite).  
3. **Restricción de Caracteres (Regex allow-list)**: Los valores de búsqueda y nombres solo pueden contener letras, números, espacios, guiones y comas: ^[a-zA-Z0-9s-.,ÁÉÍÓÚáéíóúÑñ]+$.  
4. **Bloqueo de Palabras Clave (SQLi Prevention)**: Si el input contiene subcadenas como --, /*, ;, UNION, SELECT, DROP, la herramienta MCP debe rechazar la ejecución inmediatamente (retornando al LLM: *"Input rejected due to security policy"*).

## **Key Entities & BigQuery Schema (Data Structures)**

### **1. Tabla: src_database.users (Usuarios Autenticados)**

Almacena el perfil de los usuarios in|ternos que interactúan con el sistema. Se actualiza (Upsert) cada vez que el backend valida un JWT de Firebase para mantener los metadatos frescos.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | REQUIRED | UID de Firebase (Primary Key). |
| email | STRING | REQUIRED | Correo electrónico principal del usuario. |
| email_verified | BOOLEAN | REQUIRED | Indica si el correo ha sido verificado en el proveedor. |
| display_name | STRING | REQUIRED | Nombre a mostrar del usuario. |
| photo_url | STRING | NULLABLE | URL de la foto de perfil (provista por Google/Firebase). |
| phone_number | STRING | NULLABLE | Número de teléfono asociado a la cuenta. |
| provider_id | STRING | NULLABLE | Proveedor de identidad (ej. 'https://www.google.com/search?q=google.com', 'password'). |
| created_at | TIMESTAMP | REQUIRED | Momento de creación en nuestra base de datos. |
| updated_at | TIMESTAMP | REQUIRED | Última vez que el usuario inició sesión o actualizó su token. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `provider_id`, `email_verified`

### **2. Tabla: src_api_transactions.authentication_log (Log de Autenticación)**

Tabla de solo inserción (append-only) para guardar la trazabilidad de cada intento de login. Se debe insertar un registro cada vez que hay un intento de autenticación.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | REQUIRED | Generado como UUID4 por backend |
| user_id | STRING | NULLABLE | Firebase UID |
| email | STRING | REQUIRED | Correo de intento |
| status | STRING | REQUIRED | SUCCESS, FAILED |
| error_message | STRING | NULLABLE | Opcional |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC) |
| ingestion_timestamp | TIMESTAMP | REQUIRED | Momento de escritura en BigQuery (DEFAULT CURRENT_TIMESTAMP()) |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `status`, `email`, `user_id`

### **3. Dataset: src_database.stores (Catálogo de tiendas principal)**

Diseñada para almacenar los datos de las tiendas de vino.
Las URLs de redes sociales se empaquetan en un JSON para evitar columnas dispersas.

| Nombre de Columna | Tipo de Dato | Restricción | Mapping desde CSV original |
| :---- | :---- | :---- | :---- |
| id | STRING | PRIMARY KEY | N/A (Generado como UUID4 por backend). |
| name | STRING | REQUIRED | Nombre |
| type | STRING | NULLABLE | Tipo (Digital, Mixta, Fisica.) |
| digital_platform | STRING | NULLABLE | Plataforma (ej. Shopify) |
| is_producer | BOOLEAN | REQUIRED | ¿Productor? (Transformar "Si" -> True, "No" -> False) |
| has_wine_club | BOOLEAN | REQUIRED | ¿Tiene club de vino? (Transformar "Si" -> True, "No" -> False) |
| representative_name | STRING | NULLABLE | Representante |
| country_code | STRING | REQUIRED | País | CO, MX, US, other countries
| country_name | STRING | REQUIRED | Nombre del País |
| state_code | STRING | NULLABLE | Estado |
| state_name | STRING | NULLABLE | Nombre del Estado |
| city_code | STRING | REQUIRED | Ciudad |
| city_name | STRING | REQUIRED | Nombre de la Ciudad |
| address | STRING | NULLABLE | Domicilio |
| contact_email | STRING | NULLABLE | Correo |
| contact_phone | STRING | NULLABLE | Teléfono |
| website_url | STRING | NULLABLE | URL | Ejemplo: https://www.cavasautto.com/
| social_media | JSON | NULLABLE | Agrupa: Instagram, Facebook, Twitter, Tik Tok, in, Youtube. |
| description | STRING | NULLABLE | Descripción |
| created_at | TIMESTAMP | REQUIRED | N/A (Generado por backend en la inserción). |
| updated_at | TIMESTAMP | REQUIRED | Actualización (Y actualizado por backend en cada PUT). |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `type`, `country_code`, `state_code`, `city_code`

### **4. Tabla: src_api_transactions.stores_log (Trazabilidad y Seguridad para el API de Stores)**

Esta tabla es de solo inserción (append-only) y es crucial para el cumplimiento normativo.
Se deben insertar registros por operaciones de lectura, escritura, actualización y borrado de registros en la tabla stores.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware en cada request HTTP. |
| performed_by_user_id | STRING | NULLABLE | UID de Firebase (Cruza con users.id). |
| performed_by_email | STRING | NULLABLE | Correo electrónico extraído del JWT. |
| transaction_api_type | STRING | CLUSTER KEY | 'GET', 'POST', 'PUT', 'DELETE'. |
| transaction_api_path | STRING | CLUSTER KEY | '/stores/search', '/stores', '/stores/{id}', '/locations', '/locations/{id}'. |
| transaction_db_type | STRING | CLUSTER KEY | 'INSERT', 'UPDATE', 'DELETE', 'SELECT'. |
| transaction_parameters | JSON | NULLABLE | Parámetros de la transacción. |
| payload_before | JSON | NULLABLE | Snapshot del registro *antes* de la mutación. (Null para INSERT). |
| payload_after | JSON | NULLABLE | Snapshot del registro *después* de la mutación. (Null para DELETE or SELECT). |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery (DEFAULT CURRENT_TIMESTAMP). |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `transaction_api_type`, `transaction_api_path`, `transaction_db_type`, `performed_by_user_id`

### **5. Dataset: src_database.locations (Catálogo de localizaciones geográficas)**

Tabla utilizada para popular selectores en el frontend y normalizar los queries.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | PRIMARY KEY | UUID v4 generado por el backend. |
| country_code | STRING | REQUIRED | Código ISO Alpha-2 (ej. 'MX'). Exactamente 2 caracteres. |
| country_name | STRING | REQUIRED | Nombre comercial (ej. 'México'). |
| state_code | STRING | NULLABLE | Estado o Provincia (ej. 'NAR'). |
| state_name | STRING | NULLABLE | Nombre del Estado o Provincia (ej. 'Nariño'). |
| city_code | STRING | REQUIRED | Abreviatura (ej. 'GDL', 'CDMX'). |
| city_name | STRING | REQUIRED | Nombre de la Ciudad. |
| created_at | TIMESTAMP | REQUIRED | Momento de creación. |
| updated_at | TIMESTAMP | REQUIRED | Momento de la última modificación. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `id`, `country_code`, `state_code`, `city_code`

### **6. Tabla: src_api_transactions.locations_log (Trazabilidad y Seguridad para el API de Locations)**

Esta tabla es de solo inserción (append-only) y es crucial para el cumplimiento normativo.
Se deben insertar registros por operaciones de lectura, escritura, actualización y borrado de registros en la tabla locations.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware en cada request HTTP. |
| performed_by_user_id | STRING | NULLABLE | UID de Firebase (Cruza con users.id). |
| performed_by_email | STRING | NULLABLE | Correo electrónico extraído del JWT. |
| transaction_api_type | STRING | CLUSTER KEY | 'GET', 'POST', 'PUT', 'DELETE'. |
| transaction_api_path | STRING | CLUSTER KEY | '/stores/search', '/stores', '/stores/{id}', '/locations', '/locations/{id}'. |
| transaction_db_type | STRING | CLUSTER KEY | 'INSERT', 'UPDATE', 'DELETE', 'SELECT'. |
| transaction_parameters | JSON | NULLABLE | Parámetros de la transacción. |
| payload_before | JSON | NULLABLE | Snapshot del registro *antes* de la mutación. (Null para INSERT). |
| payload_after | JSON | NULLABLE | Snapshot del registro *después* de la mutación. (Null para DELETE or SELECT). |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery (DEFAULT CURRENT_TIMESTAMP). |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `transaction_api_type`, `transaction_api_path`, `transaction_db_type`, `performed_by_user_id`

## **Success Criteria *(mandatory)***

### **Layer 1: Measurable Outcomes (Business Result)**

* **SC-001**: 100% de las mutaciones validan el JWT de Firebase, insertan/actualizan al usuario temporalmente en `src_database.users` y además registran el desenlace del evento de autenticación (status, email de intento, errores) de forma correcta en `src_api_transactions.authentication_log`.

### **Layer 2: API & Search Performance**

* **Target Latency**: Los endpoints GET generales y de búsqueda con parámetros combinados (name, city, state, country) deben responder en < 250ms en el 95% de los casos (P95).  
* **Pagination Safety**: 0 incidentes de agotamiento de memoria del servidor, garantizando que el parámetro limit nunca exceda los 100 registros por página en las APIs GET y que la estructura de metadatos de respuesta sea consistente.

### **Layer 3 & 4: Data Quality and Operational Readiness**

* **Data Quality (Updates)**: 100% de los PUT exitosos modifican únicamente la fila solicitada mediante el UUID primary key.  
* **Operational Readiness (MCP Security)**: 100% de los intentos de *Prompt Injection* (SQL injection payloads) a través del MCP son interceptados y bloqueados por las validaciones Regex en la capa de entrada, sin realizar ejecuciones en BigQuery.