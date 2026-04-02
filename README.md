# Que Vino!? Backend Micro-Swarms (v1.5.2)

Arquitectura de microservicios independientes (micro-swarms) para la plataforma **Que Vino!?**. Este repositorio gestiona el ecosistema de APIs encargadas de la comunidad vinícola, e-commerce, logística y asesoría experta con IA.

## 🚀 Arquitectura "Agentic"

Cada microservicio se despliega de forma independiente en **Google Cloud Run** y está diseñado bajo los principios de *Agentic Software Architecture*. Esto significa que cada servicio expone:
1. **API REST**: Para consumo tradicional por clientes web/móvil.
2. **Servidor MCP (Model Context Protocol)**: Permitiendo que agentes de IA utilicen estas APIs como herramientas nativas.
3. **Auditoría Nativa**: Registro automático de cada transacción en **Google BigQuery**.

### Microservicios Disponibles:

| Servicio | URL Producción | Repositorio | Descripción |
| :--- | :--- | :--- | :--- |
| **Stores API** | `https://quevino-stores-2lkhisz2aa-uc.a.run.app` | `apis/stores/` | Gestión centralizada de marcas y tiendas. |
| **Locations API** | `https://quevino-locations-2lkhisz2aa-uc.a.run.app` | `apis/locations/` | Catálogo de sucursales físicas y horarios. |
| **Knowledge Stores API** | `https://quevino-knowledge-stores-678275032484.us-central1.run.app` | `apis/knowledge_stores/` | Gestión de RAG (Red de Conocimiento) con Gemini File Search. |
| **Audio API** | `https://quevino-audio-678275032484.us-central1.run.app` | `apis/audio/` | Generación de voz (TTS) enriquecida. |

---

## 🛠️ Stack Tecnológico
- **Lenguaje**: Python 3.12+ (FastAPI)
- **Infraestructura**: Google Cloud Platform (Cloud Run, GCS, BigQuery, Vertex AI)
- **Identidad**: Firebase Authentication (Google Identity Platform)
- **Agentes**: FastMCP SDK
- **Dependencias**: Poetry
- **CORS**: Soporte oficial para `quevino.mx`, `lovable.app` y `lovableproject.com`.

---

## 🔒 Seguridad y Autenticación (Auth)

Todas las APIs requieren un **Firebase ID Token** válido en el header `Authorization`.

### Cómo obtener un Token:
Si posees las credenciales (email/password) y la `FIREBASE_API_KEY`:

**Endpoint**: `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[FIREBASE_API_KEY]`

---

## 📜 Inventario de Herramientas (OpenClaw)
Para una lista detallada de todos los endpoints, parámetros y esquemas de datos:
👉 [OPENCLAW_TOOLS.md](file:///Users/gustavovelazuniga/Desarrollo/que-vino-backend/OPENCLAW_TOOLS.md)

---
© 2026 Que Vino!? - Configurado bajo la Constitución v1.5.1.
