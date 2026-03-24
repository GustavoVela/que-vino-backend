# Que Vino Backend Constitution

Este documento define el ADN técnico, los principios inquebrantables y los estándares de calidad para el desarrollo del backend de **Que Vino!?**.

**Que Vino!?** es una comunidad de vinos diseñada para ayudar a los usuarios a comprar y aprender sobre el mundo del vino. Cuenta con agentes inteligentes (Swarms) que asisten a los usuarios en la elección de dónde comprar sus vinos basándose en presupuestos, estilos y maridajes (comidas). La plataforma ofrece servicios de sommelier digital, venta de vinos, contenido de valor, quizzes interactivos y recomendaciones personalizadas.

## 1. Stack Tecnológico & Versiones (Innegociable)

* **Lenguaje:** Python 3.12+ (Tipado estricto obligatorio).  
* **Framework Web:** FastAPI (Usado para exponer tanto Tools como Agentes).  
* **Gestor de Paquetes:** Poetry (Gestión determinista).  
* **Base de Datos ÚNICA:** **Google BigQuery** (Prohibido el uso de PostgreSQL, MySQL, Redis o cualquier tipo de caché).  
* **Despliegue:** Google Cloud Run (Despliegue unitario y autónomo por API/Agente).  
* **Frameworks Core:** **Anti Gravity**, **Spec Kit** y **ADK** (Obligatorios para la estructura y especificación. Si se deben crear agentes, estos tendrán que crearse con ADK de Google).  
* **IA & LLM:** Vertex AI SDK / Modelos Gemini (Invocados desde la configuración central).  
* **Autenticación:** **Google Auth** (Verificación de tokens de cuentas de Google/Firebase).  
* **Testing:** Pytest.

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
│   ├── sommelier/              # Agente experto en vinos y maridajes
│   │   ├── config.py           # Configuración específica de este agente
│   │   ├── prompts/            # Prompts en Markdown (.md) para este agente
│   │   ├── database/           # Archivos locales de operación (ej. CSVs locales requeridos)
│   │   ├── schemas/            # Definición de tablas BigQuery en código Python  
│   │   ├── tests/              # Pruebas específicas para este agente  
│   │   ├── deploy/             # Scripts/Dockerfile para desplegar SOLO este agente  
│   │   └── main.py             # Lógica y endpoints  
│   └── customer_support/       # Soporte al cliente inteligente
│       └── ...  
├── apis/                       # APIs de negocio y utilitarias (Micro-Tools)
│   ├── wines/                  # Gestión del catálogo de vinos y stock
│   │   ├── config.py           # Configuración específica de esta API
│   │   ├── database/           # Archivos locales de operación (ej. CSVs locales requeridos)
│   │   ├── schemas/            # Definición de tablas BigQuery en código Python  
│   │   ├── tests/              # Pruebas específicas para esta API  
│   │   ├── deploy/             # Scripts/Dockerfile para desplegar SOLO esta API  
│   │   └── main.py             # Lógica y endpoints  
│   ├── events/                 # Gestión de catas, lanzamientos y eventos  
│   │   └── ...
│   ├── grapes/                 # Información detallada de variedades de uva
│   │   └── ...
│   ├── producers/              # Directorio de bodegas y productores aliados
│   │   └── ...
│   └── regions/                # Zonas geográficas y denominaciones de origen
│       └── ...
├── docs/                       # Documentación adicional  
└── README.md                   # Índice general del proyecto

*Nota: Las APIs de negocio en `/apis/` actúan como **Tools** que pueden ser consumidas tanto por el frontend como por los propios **Agentes**.*

## 3. Configuración y Secretos Distribuidos

* **Archivo de Configuración Local:** Cada API y cada Agente **DEBE** tener su propio archivo `config.py` dentro de su carpeta raíz. Este archivo carga y valida las variables necesarias para el microservicio.
* **Secretos y Constantes Globales (`.env`):** Las constantes globales como API Keys, credenciales de BigQuery (Service Accounts), tokens de autenticación y secretos sensibles se almacenarán en un archivo `.env` en la raíz del proyecto.
* **Inyección de Dependencias:** El archivo `config.py` de cada módulo leerá desde el entorno (mediante herramientas como `pydantic-settings` o `python-dotenv`) para exponer los valores necesarios como constantes de módulo.
* **Protección Productiva:** En entornos de producción, se prohíbe el uso de archivos `.env`. Las variables DEBEN inyectarse mediante **Google Cloud Secret Manager**.

## 4. Autenticación y Seguridad

* **Método:** Autenticación obligatoria mediante correos de Google (Google Auth / Firebase Auth con proveedor Google).  
* **Datos de Prueba:** Los archivos `config.py` locales pueden contener configuraciones de prueba o leer de un `.env` específico para facilitar la ejecución de tests sin bloqueo de autenticación.

## 5. Convenciones de Código y Manejo de Errores

* **Idioma de Código:** Inglés (Variables, Clases, Funciones).  
* **Idioma de Comentarios/Docs:** **ESPAÑOL**.  
* **Type Hinting:** 100% cobertura (mypy estricto).  
* **Manejo de Errores (Crítico):**  
  * **Prohibido:** Retornar errores 500 genéricos no controlados o respuestas en texto plano.  
  * **Obligatorio:** Cada API deberá contar con un manejo apropiado y detallado de códigos HTTP (400, 401, 402, 403, 404, 409, 422, 429).  
  * **Esquema JSON Obligatorio:** Toda excepción debe ser atrapada y devuelta en el formato: `{ "error_code": "...", "message": "...", "detail": "..." }`.

## 6. Estándares de Base de Datos (BigQuery Exclusivo)

Al no existir bases de datos transaccionales clásicas ni cachés, BigQuery es el corazón de los datos.

1. **Lectura/Escritura Directa:** Todo se opera directamente hacia BigQuery mediante el SDK de Google Cloud.  
2. **Esquemas Descentralizados en Python:** **NO existen archivos .sql globales.** Cada agente o API definirá la estructura de sus tablas (esquemas) utilizando código Python dentro de su propia subcarpeta `schemas/`.  
3. **Entidades por Tabla:** En el código se creará una **entidad única por cada tabla** en archivos independientes nombrados exactamente como la tabla. Esto garantiza orden y trazabilidad.  
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
   * **Cuenta de Servicio Cloud Run:** Todos los servicios desplegados en Cloud Run deben configurarse para usar la cuenta de servicio específica: `google-antigravity@gallery-pilot-170326.iam.gserviceaccount.com`.
   * **Staging de Cloud Build:** Para evitar la creación de buckets temporales y optimizar costos, todos los despliegues vía Cloud Build deben utilizar obligatoriamente el bucket de staging: `gs://gallery-pilot-170326-cloudbuild`.

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

1. El código pasa linters y la carpeta interna `/tests/` ejecuta exitosamente.  
2. **Manejo de Errores:** Se han mapeado explícitamente los códigos HTTP de respuesta.  
3. **Esquemas en Python:** La carpeta `/schemas/` contiene la definición exacta de las tablas de BigQuery necesarias.  
4. **Deploy Unitario:** La carpeta `/deploy/` está completa y cuenta con una cuenta de servicio asignada.  
5. **Autenticación:** El endpoint valida el token de Google Auth correctamente.  
6. **Documentación (Commit Rule):** El README local y general han sido actualizados, incluyendo ejemplos de cURL.
7. **Prompts:** Si el módulo usa IA, los prompts deben estar en archivos `.md` dentro de la carpeta `/prompts/`.

## 10. Gestión de Prompts (Prompts as Code)

Para garantizar la mantenibilidad y la iteración rápida de la lógica de IA:

1. **Archivos Separados:** Está **PROHIBIDO** embeber prompts largos directamente en el código Python (`main.py`).  
2. **Formato Markdown:** Los prompts deben residir en archivos con extensión `.md`. Esto permite una mejor lectura, versionado y edición profesional.  
3. **Carpeta de Prompts:** Cada Agente o Tool que utilice IA **DEBE** tener una carpeta interna llamada `prompts/`.  
4. **Estructura y Nomenclatura:** Dentro de `prompts/`, los archivos deben nombrarse de forma descriptiva (ej. `system_prompt.md`, `extraction_logic.md`).  
5. **Inyección Dinámica:** El código Python debe cargar estos archivos Markdown y realizar las sustituciones de variables necesarias antes de enviarlos al modelo.

**Version**: 1.4.0 | **Ratified**: 17 de marzo de 2026 | **Last Amended**: 23 de marzo de 2026