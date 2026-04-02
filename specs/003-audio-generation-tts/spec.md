# **Feature Specification: Generación de Audio Multi-Proveedor (TTS API)**

**Feature Branch**: 003-que-vino-audio-generation

**Created**: 2026-04-01

**Status**: Completed

**Input**: User description: "Actualización de requerimientos: GCS para auditoría histórica, ID de proveedor como parámetro, uso de Gemini para enriquecimiento de etiquetas de ElevenLabs, y logueo completo de transacciones de la API."

**Target Persona (Primary)**: Desarrollador Frontend / Desarrollador Móvil (Consumidores de la API).

**Target Persona (Secondary)**: Agentes IA (MCP) / Data Engineer / Administrador de la Plataforma.

## **Executive Context & Market Opportunity *(mandatory)***

**Problem Statement:** Actualmente, las interacciones de los usuarios y agentes de IA en "Que Vino" están limitadas a texto. Para ofrecer una experiencia inmersiva, accesible y de alta gama (ej. lectura de notas de cata o respuestas conversacionales de agentes), necesitamos incorporar capacidades de Text-to-Speech (TTS). Depender de un solo proveedor limita nuestra flexibilidad en costos y calidad vocal. Por ello, requerimos construir una API unificada en Cloud Run que actúe como un *Gateway* hacia múltiples motores de síntesis de voz (inicialmente ElevenLabs y Google), estandarizando las peticiones. Es crucial que cada generación se almacene en Google Cloud Storage **para mantener un registro histórico inmutable que permita realizar auditorías de lo que se ha generado**, garantizando además una trazabilidad absoluta de los costos, consumos y respuestas en BigQuery.

## **Clarifications**

### **Session 2026-04-01**
- **Q: ¿Cómo se entrega el audio generado al cliente?** → **A: Binario Directo**. La API devolverá el archivo de audio completo en el cuerpo de la respuesta (`audio/mpeg` o similar) junto con el `X-Generation-ID` en los headers, evitando el uso de URLs públicas o firmadas para el acceso inmediato.
- **Q: ¿Qué formatos de audio soporta el Gateway?** → **A: mp3 y wav**. El Gateway estandariza la salida a estos dos formatos universales, mapeándolos a los equivalentes de cada proveedor para asegurar compatibilidad.
- **Q: ¿Cuál es la política para el logueo de textos con PII?** → **A: Log Completo**. Se ha decidido guardar el texto original y el procesado íntegramente en BigQuery para auditoría técnica 1:1, asumiendo el uso interno del sistema.
- **Q: ¿Cómo se manejan los IDs de voz en el Gateway?** → **A: IDs Nativos**. Se utilizan los identificadores directos de cada proveedor (ej. `rachel`, `en-US-Studio-B`), sin prefijos ni alias, para mayor transparencia.
- **Q: ¿Qué sucede si Gemini falla al enriquecer el audio?** → **A: Éxito Detallado (201 + Header)**. El sistema genera el audio con el texto original, devuelve un código **201 Created** con el header `X-Enrichment-Status: FAILED`, y registra el estatus `SUCCESS_WITHOUT_ENRICHMENT` en BigQuery.

**Out of Scope (Non-Goals):** * Creación de interfaces gráficas (Frontend) para la reproducción o gestión de los audios.

* Streaming de audio en tiempo real vía WebSockets (la API devolverá el archivo generado o su URL).  
* Entrenamiento o clonación de nuevas voces personalizadas (se utilizarán únicamente las voces preexistentes en los catálogos de los proveedores).  
* Facturación directa al usuario final por el consumo de segundos de audio.

## **User Scenarios & Testing *(mandatory)***

### **User Story 1 - Autenticación y Delegación de Identidad (Priority: P0)**

Como sistema de seguridad central de "Que Vino", quiero requerir autenticación mediante Google/Firebase para cualquier solicitud a la API de Audio, verificando la validez del token y asegurando la trazabilidad absoluta de quién consume los recursos y créditos.

**Why this priority**: Es el estándar de seguridad definido (PRD-001 y PRD-002). No podemos exponer endpoints que consumen créditos de pago (ElevenLabs/Google) ni recursos de almacenamiento sin saber qué usuario ejecuta la acción.

**Independent Test**: Can be fully tested by enviando peticiones con y sin token JWT en el header Authorization, verificando que los rechazos no consuman cuota de los proveedores y que se registre en src_api_transactions.authentication_log.

**Acceptance Scenarios**:

1. **Given** una petición a cualquier endpoint de /audio sin token JWT, **When** el middleware la intercepta, **Then** responde con **401 Unauthorized** y registra asíncronamente un FAILED en el log de autenticación.  
2. **Given** un token JWT válido de Firebase, **When** el usuario realiza una petición, **Then** el sistema permite el paso, actualiza el perfil en src_database.users si es necesario, y registra el intento exitoso.

### **User Story 2 - Consulta Unificada de Voces, Modelos y Formatos (Priority: P1)**

Como Desarrollador o Agente IA, quiero consultar los catálogos disponibles (modelos, formatos y voces) a través de endpoints de utilería que unifiquen las respuestas de Google y ElevenLabs, para poder construir interfaces de selección dinámicas sin tener que lidiar con las APIs de terceros directamente.

**Why this priority**: Para generar un audio, el cliente primero necesita saber qué provider, voice_id y format enviar. La unificación reduce la lógica en el frontend.

**Independent Test**: Can be fully tested by ejecutando peticiones GET a los endpoints de configuración y validando que el payload JSON contenga listas combinadas y mapeadas correctamente.

**Acceptance Scenarios**:

1. **Given** un usuario autenticado que solicita GET /audio/providers/models, **When** la API procesa la solicitud, **Then** responde con **200 OK** y una lista unificada de modelos disponibles indicando a qué proveedor pertenecen, registrando la transacción en el log de la API.  
2. **Given** una solicitud a GET /audio/providers/voices, **When** la API consulta internamente (o desde caché) a Google y ElevenLabs, **Then** responde con **200 OK** y un arreglo combinando las voces de ambas plataformas, estandarizando campos (ej. provider, voice_id, name, language).

### **User Story 3 - Generación de Audio, Enriquecimiento vía Gemini y Almacenamiento (Priority: P1)**

Como aplicación cliente, quiero enviar un texto a la API especificando parámetros explícitos (proveedor, voz, formato), para que el sistema genere el audio, aplique procesamiento de IA (Gemini) si requiero enriquecimiento de etiquetas expresivas (ElevenLabs), guarde el resultado como histórico en un bucket para auditoría y me devuelva el archivo, registrando toda la transacción.

**Why this priority**: Es el core del producto. Controlar explícitamente el proveedor asegura flexibilidad. El uso de Gemini para enriquecimiento automatiza la inclusión de SSML o etiquetas propias de ElevenLabs sin cargarle esta lógica al frontend. El almacenamiento garantiza el cumplimiento de auditoría.

**Independent Test**: Can be fully tested by enviando un payload válido con y sin la bandera enrich_audio, verificando la existencia del audio en GCS y la validación de las conversiones de texto en la base de datos.

**Acceptance Scenarios**:

1. **Given** un payload válido con text, provider, voice_id, y output_format, **When** se envía un POST /audio/generate, **Then** el sistema rutea la petición al proveedor especificado, genera el audio, lo guarda en Cloud Storage con un UUID como registro histórico, inserta el log en BigQuery y devuelve el audio con código **201 Created**.  
2. **Given** un payload que incluye enrich_audio: true destinado a ElevenLabs (ej. provider: "ELEVENLABS"), **When** se procesa la solicitud, **Then** el sistema invoca internamente a Gemini para inyectar etiquetas expresivas `[tag]`, envía este texto enriquecido a ElevenLabs, almacena ambas versiones y devuelve el audio.  
3. **Given** un payload que incluye enrich_audio: true destinado a Google Cloud (ej. provider: "GOOGLE"), **When** se procesa la solicitud, **Then** el sistema invoca a Gemini para inyectar etiquetas **SSML** nativas (`<emphasis>`, `<prosody>`), envía el XML resultante a Google TTS, y devuelve el binario de audio resultante.  
4. **Given** que el audio se generó exitosamente, **When** se guarda en Google Cloud Storage, **Then** el nombre del archivo debe ser exactamente el mismo UUID (id) que se registra como llave primaria en las tablas de BigQuery, garantizando la trazabilidad para auditorías.

### **User Story 4 - Manejo de Límites de Crédito y Errores del Proveedor (Priority: P2)**

Como Administrador de la Plataforma, quiero que el sistema maneje de forma elegante los fallos de los proveedores externos para no crashear la aplicación cliente y dejar un rastro claro para el equipo de operaciones.

**Why this priority**: Protege la experiencia del usuario final y alerta sobre fallos críticos operativos.

**Independent Test**: Can be fully tested by simulando (mocking) una respuesta HTTP 402 o 401 del proveedor y verificando la respuesta de nuestra API.

**Acceptance Scenarios**:

1. **Given** una petición de generación hacia ElevenLabs, **When** la cuenta se ha quedado sin créditos y el proveedor responde con un error, **Then** el sistema aborta, no guarda archivo en GCS, registra el evento con estatus ERROR_OUT_OF_CREDITS en BigQuery, guarda el payload de respuesta de error en el log de la API, y responde al cliente con **402 Payment Required**.  
2. **Given** una caída de la API de Google/ElevenLabs o de Gemini (durante el enriquecimiento), **When** se intenta procesar, **Then** el sistema falla limpiamente tras reintentos, registra el error y responde **502 Bad Gateway**.

### **Edge Cases**

* **Texto excede los límites:** Si el cliente envía un payload con un text que supera los límites de caracteres del proveedor (ej. > 5000), la API rechaza la petición inmediatamente con **422 Unprocessable Entity**.  
* **enrich_audio con proveedor incompatible:** Si se envía enrich_audio: true pero el provider es Google (que no soporta las mismas etiquetas de SSML dinámicas que ElevenLabs), el sistema ignora el flag (fallback) o rechaza con 400 detallando la incompatibilidad.  
* **Fallo en Gemini durante enriquecimiento:** Si el modelo de Gemini falla o tiene un timeout al intentar enriquecer el texto, el sistema aplica *graceful degradation* enviando el texto original al proveedor de TTS, devuelve el audio con un header de aviso (`X-Enrichment-Status: FAILED`) y registra el evento con estatus `SUCCESS_WITHOUT_ENRICHMENT`.

## **Requirements *(mandatory)***

### **Functional Requirements**

* **FR-001**: El sistema DEBE exponer endpoints GET para listar: Modelos, Formatos de audio y Voces, combinando los catálogos de Google y ElevenLabs.  
* **FR-002**: El sistema DEBE exponer un endpoint POST /audio/generate que acepte los parámetros obligatorios: `text` (máx. 5000 chars), `provider` (ELEVENLABS | GOOGLE), `voice_id`, `output_format` (mp3 | wav) y el opcional `enrich_audio` (booleano).  
* **FR-003**: El sistema DEBE almacenar *cada* archivo de audio generado exitosamente en un bucket de Google Cloud Storage como registro histórico inmutable para auditorías.  
* **FR-004**: El archivo en el bucket DEBE nombrarse usando un UUID v4 (ej. [UUID].[format]).  
* **FR-005**: Si enrich_audio es true, el sistema DEBE enviar el texto a Gemini para inyectar marcas de prosodia nativa según el proveedor:
    - **ElevenLabs**: Inyectar Audio Tags `[tag]`.
    - **Google TTS**: Inyectar marcado SSML `<speak>`.
    Ambas versiones del texto (original y enriquecido) DEBEN registrarse en BigQuery.  
* **FR-006**: El sistema DEBE registrar de manera síncrona/asíncrona todas las peticiones a la API (incluyendo parámetros, payloads enviados y recibidos) en BigQuery.

### **Non-Functional Requirements & AI Guardrails**

* **NFR-001 - Security (Secret Management):** Las claves de API de ElevenLabs, Google y Gemini DEBEN almacenarse en Secret Manager o .env aislados. **NUNCA** se devolverán al frontend.  
* **NFR-002 - Concurrency & Scalability:** El despliegue en Cloud Run debe ser asíncrono para manejar las latencias combinadas (Gemini + TTS Provider) sin bloquear hilos del servidor.  
* **NFR-003 - Performance:** Las peticiones de utilería (List Voces) deben responder en < 300ms (usando caché).  
* **NFR-004 - Data Integrity:** Guardar el archivo en GCS es obligatorio para la trazabilidad. Si la escritura en el Bucket falla, la transacción debe ser marcada como fallida aunque el proveedor haya entregado el audio.

### **The Three-Tier Boundaries**

* **Always do:** Validar el token JWT de Firebase y registrar cada transacción en la tabla de logs de la API para mantener visibilidad completa de las peticiones y respuestas.  
* **Ask first:** Implementar alertas (Cloud Monitoring) si el consumo de créditos (rechazos 402) o fallos de Gemini superan umbrales predefinidos.  
* **Never do:** Nunca eliminar o sobrescribir audios previos en Cloud Storage. El Bucket es de tipo *append-only* (solo lectura/escritura inicial) para mantener la integridad de la auditoría.

## **Data Structures, Telemetry & Transactional Auditing**

Alineado a los estándares de "Que Vino" (spec-001), se requiere trazabilidad transaccional estricta.

### **1. Tabla: src_api_transactions.audio_api_log (Log General de la API)**

Esta tabla es de solo inserción (append-only) y captura el detalle completo (peticiones y respuestas) de todas las interacciones HTTP contra los endpoints de audio.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware por cada request. |
| performed_by_user_id | STRING | NULLABLE | UID de Firebase (Cruza con users.id). |
| transaction_api_type | STRING | CLUSTER KEY | 'GET', 'POST'. |
| transaction_api_path | STRING | CLUSTER KEY | '/audio/generate', '/audio/providers/voices', etc. |
| transaction_parameters | JSON | NULLABLE | Query parameters de la petición (ej. filtros de búsqueda). |
| payload_request | JSON | NULLABLE | Cuerpo completo de la solicitud original del cliente. |
| payload_response | JSON | NULLABLE | Cuerpo de la respuesta entregada (incluyendo mensajes de error de proveedores si falló). |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery. |

**Configuración de Optimización:**

* **Particionamiento:** ingestion_timestamp (por día).  
* **Clusterización:** transaction_api_type, transaction_api_path, performed_by_user_id.

### **2. Tabla: src_api_transactions.audio_generation_log (Auditoría Específica de Generación)**

Registra el detalle del negocio sobre los audios generados y los consumos de IA, cruzando los identificadores del bucket.

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| generation_id | STRING | PRIMARY KEY | UUID v4. **Debe ser exactamente el nombre del archivo en el Bucket GCS.** |
| api_transaction_id | STRING | REQUIRED | FK hacia audio_api_log.transaction_id. |
| performed_by_user_id | STRING | REQUIRED | UID del solicitante. |
| provider | STRING | REQUIRED | 'ELEVENLABS', 'GOOGLE'. |
| voice_id | STRING | REQUIRED | Identificador de la voz. |
| is_enriched | BOOLEAN | REQUIRED | ¿Se solicitó y logró el enriquecimiento vía Gemini? |
| text_input | STRING | REQUIRED | Texto original del cliente. |
| text_processed | STRING | NULLABLE | Texto con etiquetas (Salida de Gemini) enviado al proveedor. |
| status | STRING | REQUIRED | 'SUCCESS', 'SUCCESS_WITHOUT_ENRICHMENT', 'ERROR_OUT_OF_CREDITS', 'ERROR_PROVIDER_DOWN'. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento de generación (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery. |

### **3. Estructura del Bucket (Cloud Storage - Histórico)**

* **Bucket Name:** que-vino-23032025-audios  
* **Pathing:** /generations/[generation_id].[output_format]  
* **Regla de Negocio:** El bucket sirve como bóveda de auditoría. No se permite la eliminación de objetos por parte de la API. Aplicar políticas de ciclo de vida (GCP Console) para mover a Coldline luego de 90 días por costos.

## **Success Criteria *(mandatory)***

### **Layer 1: Measurable Outcomes (Business Result)**

* **SC-001 (Unified & Explicit Integration)**: 100% de las solicitudes de generación son procesadas respetando el provider enviado por el cliente, devolviendo el archivo binario directamente en la respuesta HTTP.  
* **SC-002 (Audit & Traceability)**: 100% de los audios almacenados en Cloud Storage poseen registros espejos en audio_generation_log y sus respectivas peticiones/respuestas HTTP detalladas en audio_api_log. El ID de generación se entrega en el header `X-Generation-ID`.

### **Layer 2: Model Performance (Gemini Enrichment)**

* **SC-003**: En peticiones con enrich_audio: true, Gemini debe retornar el texto con las etiquetas correctas de ElevenLabs en < 1.5 segundos en el 90% de los casos, evitando penalizar severamente la latencia general de la generación de voz.

### **Layer 3 & 4: Data Quality and Operational Readiness**

* **Data Quality**: 100% de los payloads fallidos y exitosos (incluidas caídas de red o fallos de créditos) están registrados en formato JSON en la columna payload_response de la tabla general de logs de la API.  
* **Operational Readiness**: El servicio en Cloud Run posee permisos IAM estrictamente limitados para escribir en el Bucket de auditoría y en las tablas de BigQuery, sin permisos de lectura externa ni eliminación (Append-only).