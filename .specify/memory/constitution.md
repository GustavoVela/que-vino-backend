# Que Vino Backend Constitution

Este documento define el ADN técnico, los principios inquebrantables y los estándares de calidad para el desarrollo del backend de **Que Vino!?**.

**Que Vino!?** es una comunidad de vinos diseñada para ayudar a los usuarios a comprar y aprender sobre el mundo del vino. Cuenta con agentes inteligentes (Swarms) que asisten a los usuarios en la elección de dónde comprar sus vinos basándose en presupuestos, estilos y maridajes (comidas). La plataforma ofrece servicios de sommelier digital, venta de vinos, contenido de valor, quizzes interactivos y recomendaciones personalizadas.

## 1. Stack Tecnológico & Versiones (Innegociable)

* **Lenguaje:** Python 3.12+ (Tipado estricto obligatorio).  
* **Framework Web:** FastAPI (Usado para exponer tanto Tools como Agentes).  
* **Gestor de Paquetes:** Poetry (Gestión determinista).  
* **Base de Datos ÚNICA:** **Google BigQuery** (Prohibido el uso de PostgreSQL, MySQL, Redis o cualquier tipo de caché).  
* **Despliegue:** Google Cloud Run (Despliegue unitario y autónomo por API/Agente).  
* **Frameworks Core:** **Anti Gravity**, **Spec Kit**, **ADK** y SDK de **MCP** (Obligatorios para la estructura agéntica, especificaciones y exposición de herramientas).  
* **IA & LLM:** Vertex AI SDK / Modelos Gemini (Invocados desde la configuración central).  
* **Gemini SDK (Moderno 2026):** Es ESTRICTAMENTE OBLIGATORIO el uso del SDK **`google-genai` (v1.70.0+)** con el patrón Native (AI Studio) para toda operación de RAG, File Search Stores e indexado masivo. El uso de librerías antiguas (`google-generativeai`) o métodos legacy queda terminantemente prohibido bajo pena de falla de cumplimiento arquitectónico.
* **Protocolos Agénticos:** Obligatorio el uso de **A2A (Agent-to-Agent)** para orquestación y **MCP (Model Context Protocol)** para herramientas.
* **Autenticación:** **Google Auth** (Verificación de tokens de cuentas de Google/Firebase).  
* **Testing:** Pytest.
* **CORS Standard:** Los microservicios deben permitir los orígenes oficiales del ecosistema (localhost, quevino.mx, lovable apps) definidos en la sección 4.2.

## 2. Filosofía de Arquitectura (Micro-Swarms y Casos de Uso)

### 2.1. Despliegue Unitario y Autónomo

El sistema abandona el concepto de monolito. Cada componente es una isla de cómputo:

* Cada **API de Negocio** y cada **Agente** es un microservicio independiente centrado en un **caso de uso** específico.  
* Se despliegan de forma paralela o autónoma en **Cloud Run**. No es necesario desplegar todo el sistema para actualizar un solo microservicio.  
* Todos los componentes deben quedar expuestos como APIs HTTP llamables.
* **Seguridad de Despliegue:** Cada despliegue en Cloud Run deberá realizarse utilizando una **cuenta de servicio única** para garantizar el cumplimiento del principio de mínimo privilegio.

### 2.2. Agentes Orientados a Casos de Uso

Los agentes no llevan nombres genéricos, sino que se nombran por el producto o resultado de su caso de uso (ej. `sommelier`, `customer_support`, `wine_recommendations`).

### 2.3. Topología de Directorios

Estructura descentralizada y estricta para garantizar la autonomía de cada componente:

/  
├── core/                       # Núcleo y utilidades compartidas (Cross-cutting)
│   ├── auth_middleware.py      # Lógica compartida de Auth Guard y validación Firebase
│   └── db_utils.py             # Helpers para BigQuery: inicialización y lógica de UPSERT (MERGE)
├── agents/                     # Casos de uso de IA y enjambres  
│   ├── summoner/               # Agente orquestador (puede haber múltiples orquestadores)
│   │   ├── agent_card.yaml     # Tarjeta de descubrimiento (OBLIGATORIO)
│   │   ├── config.py
│   │   ├── deploy/
│   │   └── main.py             # Enruta y maneja flujos lógicos usando A2A
│   ├── sommelier/              # Agente experto en vinos y maridajes
│   │   ├── agent_card.yaml     # Tarjeta de descubrimiento en la red A2A (OBLIGATORIO)
│   │   ├── config.py           # Configuración específica de este agente
│   │   ├── prompts/            # Prompts en Markdown (.md) para este agente
│   │   ├── database/           # Archivos locales de operación (ej. CSVs)
│   │   ├── tests/              # Pruebas específicas para este agente  
│   │   ├── deploy/             # Scripts/Dockerfile para desplegar SOLO este agente  
│   │   └── main.py             # Lógica de orquestación y del agente  
│   └── customer_support/       # Soporte al cliente inteligente
│       └── ...  
├── apis/                       # APIs de negocio (Consumo UI/Admin) y utilitarias (MCP)
│   ├── wines/                  # Gestión del catálogo de vinos y stock
│   │   ├── config.py           # Configuración específica de esta API
│   │   ├── database/           # Archivos locales de operación (ej. CSVs requeridos)
│   │   ├── schemas/            # Definición de tablas y configuración para BigQuery
│   │   ├── tests/              # Pruebas específicas para esta API  
│   │   ├── deploy/             # Scripts/Dockerfile para desplegar SOLO esta API  
│   │   ├── mcp_server.py       # Exposición de la capa de API como Servidor MCP (Para Agentes)
│   │   └── main.py             # Capa de API tradicional REST/FastAPI (Para UI / Admins)
│   ├── regions/                # Mantenimiento de regiones. Ex: Admin UI manipula regions vía main.py
│   │   └── ...                 #   y los Agentes la leen/consultan vía mcp_server.py
│   └── events/                 # Gestión de eventos
│       └── ...
├── setup/                      # Scripts globales de configuración (ej. setup_bq.py)
├── docs/                       # Documentación adicional  
└── README.md                   # Índice general del proyecto

*Nota: Las APIs de negocio en `/apis/` actúan como **Tools** que pueden ser consumidas tanto por el frontend como por los propios **Agentes**.*

### 2.4. Arquitectura Agéntica Distribuida

La arquitectura del sistema se basa en la creación de un ecosistema distribuido y escalable, alejándose de los "agentes monolíticos" que intentan resolver todo por sí mismos. Esta estructura se divide en cuatro capas fundamentales: desacoplamiento de herramientas, especialización de agentes, orquestación mediante microservicios y gobernanza.

1. **Desacoplamiento de Herramientas con MCP (Model Context Protocol)**
   En lugar de programar herramientas directamente dentro del código del agente, se utiliza el estándar MCP para separar la lógica de las herramientas de la lógica del agente. Esto permite que múltiples agentes consuman las mismas herramientas sin duplicar código. Se definen tres tipos de servidores de herramientas:
   * **Patrón Imperativo (APIs externas):** Define la lógica paso a paso para conectar con servicios de terceros, permitiendo limpiar o transformar los datos antes de entregarlos al agente.
   * **Patrón Determinístico (Funciones generales):** Utilizado para cálculos matemáticos o lógica personalizada que no requiere red, garantizando resultados consistentes.
   * **Patrón Declarativo (Bases de Datos):** Utiliza la MCP Toolbox para Bases de Datos. Mediante archivos de configuración YAML, se exponen consultas (ej. SQL/BigQuery) como herramientas seguras sin escribir código de conexión explícito.

2. **Agentes Especializados con ADK (Agent Development Kit)**
   La arquitectura propone el uso del ADK para implementar patrones de diseño específicos en el flujo de trabajo de cada agente, en lugar de confiar en que un solo modelo resuelva procesos complejos:
   * **Secuencial:** Ideal para procesos con dependencias lineales donde la salida del paso A es la entrada obligatoria del paso B.
   * **Paralelo:** Utiliza un patrón fan-out/fan-in para ejecutar múltiples tareas simultáneamente (como consultar varias APIs a la vez) y luego sintetizar los resultados.
   * **Bucle (Loop):** Permite que el agente itere sobre una tarea hasta que se cumpla una condición específica o se alcance un límite de intentos.
   * **Enrutamiento Jerárquico:** Un flujo probabilístico donde un agente analiza la situación y decide qué sub-agente es el más apto para el caso.

3. **Orquestación y Microservicios (Protocolo A2A)**
   Para evitar que el sistema sea un bloque rígido de código, se emplea el protocolo Agent-to-Agent (A2A). Este transforma los scripts de los agentes en microservicios descubribles a través de la red.
   * **Agent Card:** Funciona como una tarjeta de presentación digital que describe el nombre, las habilidades y la URL de cada agente.
   * **Summoner Agent (Orquestador):** Este agente actúa como un estratega central. No ejecuta lógica de negocio, sino que utiliza el "Descubrimiento de Servicios" para leer las Agent Cards disponibles en la red y decidir dinámicamente a qué agente llamar según la petición del usuario.

4. **Gobernanza y Memoria de Estado**
   Para asegurar que el sistema sea robusto y cumpla con reglas de negocio, se implementan interceptores mediante el ADK:
   * **Callbacks y Plugins:** Permiten interceptar el proceso de pensamiento del agente para aplicar reglas como límites de tasa (rate limits) o periodos de enfriamiento (cooldowns) sin modificar el código base del agente.
   * **Estado de Corto Plazo:** El orquestador mantiene una "memoria de sesión" (actualizada mediante *after-tool callbacks*) para recordar qué agentes se usaron recientemente. Esto evita llamar repetidamente al mismo agente si el sistema requiere rotación o diversidad.

*Nota: Este diseño permite que los equipos de datos gestionen las consultas, los equipos de backend las APIs y los desarrolladores de IA los flujos de forma totalmente independiente y segura.*

### 2.5. Infraestructura Cloud (Google Cloud)

Para profundizar en la arquitectura descrita, se integran explícitamente herramientas y servicios de Google Cloud que actúan como la infraestructura base para que los protocolos (MCP y A2A) y los agentes funcionen de manera profesional y escalable:

1. **Infraestructura de Ejecución: Google Cloud Run**
   Es la pieza central de esta arquitectura. Todos los componentes (servidores MCP y agentes A2A) se despliegan como contenedores en Cloud Run.
   * **Por qué se usa:** Permite que cada agente funcione como un microservicio independiente. Es serverless, escalando y consumiendo recursos solo cuando un agente es llamado por el orquestador o usuario.
   * **Detalle técnico:** Cloud Run proporciona la URL pública (endpoint) necesaria para que el protocolo A2A pueda realizar el "descubrimiento de servicios".

2. **Capa de Datos: BigQuery (Adaptación del patrón Librarium)**
   Aunque los patrones agénticos estándar suelen ejemplificar con Cloud SQL (Librarium), **Que Vino!?** se apoya exclusivamente en **Google BigQuery**.
   * **Integración:** Se utiliza un modelo similar a "MCP Toolbox" adaptado a BigQuery, abstrayendo la conexión subyacente de operaciones complejas.
   * **Seguridad:** El servidor/API actúa como un puente seguro entre el agente y BigQuery, asegurando que el agente solo ejecute rutinas controladas y esquematizadas.

3. **Inteligencia y Modelos: Gemini (Vertex AI)**
   La inteligencia que impulsa a cada "familiar" o agente proviene de Gemini.
   * **Vertex AI:** Plataforma donde residen los modelos. El ADK interactúa con las APIs de Vertex AI para razonar, invocar herramientas y procesar lenguaje natural.

4. **Automatización y Despliegue: Cloud Build**
   Transfoma los scripts en servicios de nube de forma automatizada.
   * **Función:** Gestiona el pipeline de CI/CD. Las actualizaciones activan Cloud Build para construir y desplegar la imagen en Cloud Run.

5. **Protocolos y Frameworks (Capa de Software)**
   * **MCP (Model Context Protocol):** Estándar abierto que actúa como traductor entre los objetivos del agente y las capacidades de las bases de datos o APIs.
   * **ADK (Agent Development Kit):** Framework para definir de manera robusta los flujos, testeándolos localmente en su interfaz web antes de producción.

**Resumen del Flujo de Trabajo Agéntico:**
* **Desarrollo:** Creación de agentes con ADK, definición de herramientas mediante MCP.
* **Despliegue:** Construcción (Cloud Build) y entrega a entornos serverless (Cloud Run).
* **Conexión:** Interacciones de datos y APIs viabilizadas por MCP hacia Google BigQuery.
* **Orquestación:** Coordinación central a través de un Summoner Agent (en Cloud Run) empleando el protocolo A2A para escalar de modo modular y no monolítico.

## 3. Configuración y Secretos Distribuidos

* **Archivo de Configuración Local:** Cada API y cada Agente **DEBE** tener su propio archivo `config.py` dentro de su carpeta raíz. Este archivo carga y valida las variables necesarias para el microservicio.
* **Secretos y Constantes Globales (`.env`):** Las constantes globales como API Keys, credenciales de BigQuery (Service Accounts), tokens de autenticación y secretos sensibles se almacenarán en un archivo `.env` en la raíz del proyecto.
* **Inyección de Dependencias:** El archivo `config.py` de cada módulo leerá desde el entorno (mediante herramientas como `pydantic-settings` o `python-dotenv`) para exponer los valores necesarios como constantes de módulo.
* **Voces por Defecto:** Toda configuración de voces (TTS) debe centralizarse en el `config.py` del microservicio respectivo, utilizando variables de entorno para su sobrescritura (ej. `DEFAULT_VOICE_ELEVENLABS`).
* **Protección Productiva:** En entornos de producción, se prohíbe el uso de archivos `.env`. Las variables DEBEN inyectarse mediante **Google Cloud Secret Manager**.

## 4. Autenticación y Seguridad

* **Método:** Autenticación obligatoria mediante correos de Google (Google Auth / Firebase Auth con proveedor Google).
* **Patrón de Middleware Global:** OBLIGATORIO utilizar una clase estándar `AuthMiddleware` heredada de `BaseHTTPMiddleware` (Starlette) en el archivo `core/auth_middleware.py` de cada API. Este middleware debe:
   1. Interceptar el 100% de las peticiones para validar el `Authorization: Bearer <TOKEN>`.
   2. Manejar de forma detallada excepciones de Firebase (ej. `ExpiredIdTokenError`, `RevokedIdTokenError`, `InvalidIdTokenError`) devolviendo el código 401 y una estructura JSON estándar, o 500 ante errores internos.
   3. Proveer de logs de auditoría asíncronos en BigQuery (`authentication_log`) tanto de éxitos como rechazos.
   4. Excluir explícitamente las rutas públicas de documentación (`/docs`, `/openapi.json`, `/redoc`) para no romper el Swagger UI.
* **CORS Standard Configuration:** Para garantizar la interoperabilidad, toda API debe configurar el `CORSMiddleware` con los siguientes orígenes:
   - `http://localhost`, `http://localhost:3000`, `http://localhost:5173`
   - `https://quevino.mx`, `https://www.quevino.mx`
    - `https://que-vino-admin.lovable.app`
    - `https://9ebf32fb-b85f-43d4-b440-af3007c90f34.lovableproject.com`
    - `https://id-preview--9ebf32fb-b85f-43d4-b440-af3007c90f34.lovable.app`
* **Datos de Prueba:** Los archivos `config.py` locales pueden contener configuraciones de prueba o leer de un `.env` específico para facilitar la ejecución de tests sin bloqueo de autenticación.

### 4.1. Prevención de Prompt Injection y Seguridad Agéntica

Dado que el ecosistema agéntico es vulnerable a vectores de ataque basados en lenguaje natural, se establecen los siguientes mecanismos de defensa obligatorios:
* **Mínimo Privilegio (Muros de Fuego Lógicos):** Ningún agente único tendrá acceso total a escritura destructiva a bases de datos o cuentas de usuario. Cada *tool* MCP expuesta en `mcp_server.py` debe estar altamente delimitada. Los esquemas declarativos en YAML previenen peticiones SQL arbitrarias por parte del LLM.
* **Sanitización e Interceptores:** El ADK deberá utilizar **Interceptores (Pre-Tool Callbacks)** para filtrar e inspeccionar cadenas de texto proporcionadas por el usuario, evitando que instrucciones maliciosas modifiquen los *system prompts* básicos o realicen *SQL/Command Injection* veladas.
* **Separación de Responsabilidades:** Las acciones potencialmente destructivas (como borrar usuarios) deben permanecer idealmente en métodos estandarizados expuestos vía `main.py` bajo alta autorización (Administradores con Auth clásico) y no estar disponibles indiscriminadamente en el `mcp_server.py` del agente sin una confirmación manual fuerte (Human-In-The-Loop).

## 5. Convenciones de Código y Manejo de Errores

* **Idioma de Código:** Inglés (Variables, Clases, Funciones).  
* **Idioma de Comentarios/Docs:** **ESPAÑOL**.  
* **Documentación Premium (Docstrings):** **OBLIGATORIO** implementar documentación de alto nivel mediante docstrings formales en todos los archivos, módulos, clases y métodos. 
    1. **Idioma:** Siempre en **ESPAÑOL** profesional.
    2. **Contenido:** Debe detallar el propósito de negocio, lógica técnica (si es compleja), descripción exhaustiva de parámetros y valores de retorno.
    3. **Calidad:** Los docstrings deben permitir que un agente de IA o un desarrollador externo entienda la función sin leer el código fuente.
* **Type Hinting:** 100% cobertura (mypy estricto).  
* **Manejo de Errores (Crítico):**  
  * **Prohibido:** Retornar errores 500 genéricos no controlados o respuestas en texto plano.  
  * **Obligatorio:** Cada API deberá contar con un manejo apropiado y detallado de códigos HTTP (400, 401, 402, 403, 404, 409, 422, 429).  
  * **Esquema JSON Obligatorio:** Toda excepción debe ser atrapada y devuelta en el formato: `{ "error_code": "...", "message": "...", "detail": "..." }`.
  * **Timeout y Limites de Tasa (API):** Es estricta la implementación de timeouts duros configurables (ej. máximo 5 segundos) para no enhebrar eternamente el hilo web, devolviendo un error controlado, junto a las mitigaciones de tasa con error *429 Too Many Requests*.
  
## 6. Estándares de Base de Datos (BigQuery Exclusivo)

Al no existir bases de datos transaccionales clásicas ni cachés, BigQuery es el corazón de los datos.

1. **Acceso Declarativo mediante MCP:** En lugar de esparcir operaciones del SDK de Google Cloud en todo el código sin control, el acceso a BigQuery se centraliza en las APIs. Estas exponen operaciones controladas de datos como herramientas mediante la **MCP Toolbox para Bases de Datos** (patrón declarativo). Los Agentes *consumen* la base de datos indirectamente usando el estándar MCP.
2. **Esquemas Descentralizados:** **NO existen archivos .sql globales.** Cada API responsable de un dominio definirá la estructura de sus tablas y las consultas pre-validadas en su propia subcarpeta `schemas/`. Estas definiciones serán el respaldo para el acceso a través de la interfaz MCP segura.
3. **Entidades por Tabla:** Existirá una **entidad única por cada tabla** gestionada dentro de su subcarpeta correspondiente, garantizando trazabilidad y control.  
4. **Optimización de Consultas (Clustering & Partitioning):** Todo esquema de tabla de BigQuery **DEBE** incluir:
   * **Particionamiento:** Un (1) campo obligatorio de particionamiento (normalmente por fecha o timestamp).
   * **Clusterización:** Hasta un máximo de cuatro (4) campos de clusterización para optimizar costos y velocidad de escaneo.
5. **Tipos de Tablas:**  
   * **Tablas de Entidades:** Guardan el estado o resultados.  
   * **Tablas de Relaciones:** Guardan relaciones entre tablas de entidades.  
   * **Tablas de Logs:** Cada Tool/Agente debe tener su propia tabla de logs transaccionales para auditoría y debug.

## 7. Pruebas y Despliegue Unitario

1. **Carpeta de Tests:** Cada utilidad (Agente o API) **DEBE** tener adentro su propia carpeta /tests/. Esto asegura que cada microservicio se pruebe de manera completamente aislada.  
2. **Carpeta de Deploy:** Cada API o agente **DEBE** tener su propia carpeta /deploy/ que contenga el Dockerfile, archivos de configuración de Cloud Run, y scripts de CI/CD específicos para explicar y ejecutar el despliegue de esa sola parte.
3. **Infraestructura Obligatoria (GCP):**
   * **Cuenta de Servicio Cloud Run:** Todos los servicios desplegados en Cloud Run deben configurarse para usar la cuenta de servicio de mínimos privilegios asignada al proyecto (ej. `cloud-run-apis@que-vino-23032025.iam.gserviceaccount.com`).
   * **Despliegue Directo:** Para los despliegues usando `cloudbuild.yaml` se DEBE utilizar obligatoriamente el bucket de Cloud Storage asignado internamente ejecutando: `gcloud builds submit --config <RUTA_YAML> --gcs-source-staging-dir=gs://que-vino-23032025-cloudbuild/source .`. Esto asegura que los archivos fuentes se empaquen y almacenen debidamente con los permisos corporativos correctos antes de la compilación en Artifact Registry / Container Registry.

## 8. Reglas de Git y Documentación Viva (Anti Gravity)

1. **Idioma de Interacción:** **ESPAÑOL**. Todos los mensajes de commit y comunicación serán en español.  
2. **Regla de Commits y Readmes:** En **CADA COMMIT** que modifique el comportamiento, contrato o estructura de un módulo, es **OBLIGATORIO** revisar y actualizar:  
   * El README.md específico del agente/API modificado.     * El README.md general (raíz del proyecto) si se agregó/eliminó un módulo o cambió su forma de acceso global.  
    * **Ejemplos de cURL:** Es **OBLIGATORIO** que cada README de API incluya ejemplos de comandos `curl` funcionales para cada endpoint, permitiendo pruebas rápidas desde la terminal.
3. **Especficación para Agentes (OPENCLAW):** Es **OBLIGATORIO** que, cada vez que se modifique un contrato de API o se actualicen los READMEs de los microservicios, se actualice el archivo `/OPENCLAW_TOOLS.md`. Este archivo es la guía de vida para agentes de IA que operarán la galería, por lo que debe contener:
   * Rutas productivas de Cloud Run actualizadas.
   * Ejemplos de uso (cURL) de cada endpoint.
   * Casos de uso detallados para la operación de la galería (onboarding, auditoría, gestión de staff, etc.).
   * Solo información productiva y de alto nivel útil para la operación.
4. **Spec Kit Compliance:** Todo API y Agente debe definir su contrato de entrada y salida claramente, permitiendo que el framework parsee y valide las especificaciones.

## 9. Definición de Hecho (Definition of Done - DoD)

Un caso de uso, API o Agente se considera terminado SOLO si:

1. El código pasa linters y la carpeta interna `/tests/` ejecuta exitosamente de forma aislada.  
2. **Manejo de Errores y Seguridad:** Se han mapeado explícitamente los códigos HTTP (APIs), mitigado escenarios de *Prompt Injection* (Agentes) y el Auth de Google es validado correctamente.
3. **Despliegue e Identidad:** La carpeta `/deploy/` está completa y cuenta con una Service Account de mínimos privilegios.
4. **Cumplimiento Agéntico (Estricto):**
   * **Agentes:** Su archivo `agent_card.yaml` debe existir y su descubrimiento A2A (*delegación*) debe comprobarse frente a un agente central (Ej. Summoner).
   * **APIs / Herramientas:** La interfaz de dominio debe estar separada limpiamente; el uso REST puro (para UI / Admins) debe residir en `main.py`, y la capa agéntica/herramientas debe residir y estar operativa en el `mcp_server.py`.
5. **Base de Datos Declarativa:** La carpeta `/schemas/` de la API posee sus definiciones de BigQuery estructuradas y listas para su integración bajo MCP Toolbox.
6. **Documentación (API y MCP):** El README debe enseñar: a) El consumo estándar de los Endpoints y b) Las capacidades expuestas en el MCP Server. El `OPENCLAW_TOOLS.md` global debe quedar actualizado acorde al cambio.
7. **Prompts:** Todo Prompt debe residir estrictamente en la carpeta `/prompts/` en formato Markdown.

## 10. Gestión de Prompts (Prompts as Code)

Para garantizar la mantenibilidad y la iteración rápida de la lógica de IA:

1. **Archivos Separados:** Está **PROHIBIDO** embeber prompts largos directamente en el código Python (`main.py`).  
2. **Formato Markdown:** Los prompts deben residir en archivos con extensión `.md`. Esto permite una mejor lectura, versionado y edición profesional.  
3. **Carpeta de Prompts:** Cada Agente o Tool que utilice IA **DEBE** tener una carpeta interna llamada `prompts/`.  
4. **Estructura y Nomenclatura:** Dentro de `prompts/`, los archivos deben nombrarse de forma descriptiva (ej. `system_prompt.md`, `extraction_logic.md`).  
5. **Inyección Dinámica:** El código Python debe cargar estos archivos Markdown y realizar las sustituciones de variables necesarias antes de enviarlos al modelo.

**Version**: 1.5.1 | **Ratified**: 17 de marzo de 2026 | **Last Amended**: 1 de abril de 2026