# Que Vino Backend Micro-Swarms

Arquitectura de microservicios independientes (micro-swarms) para la plataforma **Que Vino!?**. Este repositorio gestiona el backend encargado de la comunidad vinícola, e-commerce y asesoría experta con IA.

## 🚀 Arquitectura

Cada microservicio se despliega de forma independiente en Google Cloud Run y está diseñado para funcionar tanto como una API REST tradicional como un servidor MCP (Model Context Protocol).

### Microservicios Actuales:
- **Stores API** (`/apis/stores`): Gestión y búsqueda de tiendas, productores y clubes de vino.
- **Locations API** (`/apis/locations`): Catálogo de localizaciones (países, estados, ciudades).

## 🛠️ Tecnologías
- **Core**: Python 3.12+, FastAPI
- **Infraestructura**: Google Cloud Run, Cloud Build
- **Base de Datos**: Google BigQuery
- **Auth**: Firebase Authentication (Google Identity)
- **Framework de Agentes**: FastMCP (Model Context Protocol)
- **Gestión de dependencias**: Poetry

## ⚙️ Configuración Global

El proyecto utiliza un archivo `.env` en la raíz para las variables de entorno compartidas:

```bash
GOOGLE_CLOUD_PROJECT="que-vino-23032025"
FIREBASE_API_KEY="..."
```

Cada microservicio carga estas variables automáticamente a través de Pydantic Settings.

## 📦 Despliegue

El despliegue está automatizado con Cloud Build. Cada servicio tiene su propia configuración de escalado (limitada por defecto a `max-instances=1`).

```bash
# Desplegar Localizaciones
gcloud builds submit --config apis/locations/deploy/cloudbuild.yaml .

# Desplegar Tiendas
gcloud builds submit --config apis/stores/deploy/cloudbuild.yaml .
```

## 🔒 Seguridad
- **CORS**: Estrictamente configurado para dominios de producción y previews de Lovable.
- **Auth Middleware**: Valida tokens de Firebase en cada petición (excepto OPTIONS para preflight).
- **Audit Logs**: Cada transacción (INSERT/UPDATE/DELETE) se registra automáticamente en BigQuery en el dataset `src_api_transactions`.

---
© 2026 Que Vino!? - Constitución y Reglas configuradas bajo los principios de Agentic Software Architecture.
