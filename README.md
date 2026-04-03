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
| **Knowledge Stores API** | `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app` | `apis/knowledge_stores/` | Gestión de RAG (Red de Conocimiento) con Gemini File Search. |
| **Audio API** | `https://quevino-audio-2lkhisz2aa-uc.a.run.app` | `apis/audio/` | Generación de voz (TTS) enriquecida. |

---

## 🛠️ Stack Tecnológico
- **Lenguaje**: Python 3.12+ (FastAPI)
- **Infraestructura**: Google Cloud Platform (Cloud Run, GCS, BigQuery, Vertex AI)
- **Identidad**: Firebase Authentication (Google Identity Platform)
- **Agentes**: FastMCP SDK + ADK
- **Dependencias**: Poetry
- **CORS**: Soporte oficial para `quevino.mx`, `lovable.app` y `lovableproject.com`.

---

## 🔒 Seguridad y Autenticación (Auth)

Todas las APIs requieren un **Firebase ID Token** válido en el header `Authorization`.

### Cómo obtener un Token:

```bash
curl -X POST \
  "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=<FIREBASE_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com", "password": "contraseña", "returnSecureToken": true}'
```

---

## 🧪 Estándar de Pruebas (Sección 7.2)

Cada microservicio incluye un script de integración estandarizado que prueba todos sus endpoints en producción y genera un reporte en Markdown.

```bash
# Pruebas de Audio API
python3 apis/audio/tests/test_production.py

# Pruebas de Knowledge Stores API
python3 apis/knowledge_stores/tests/test_production.py
```

Cada script genera su propio `tests/TEST_RESULTS.md` con los llamados HTTP completos y las respuestas de producción.

---

## 📜 Inventario de Herramientas (OpenClaw)
Para una lista detallada de todos los endpoints, parámetros y esquemas de datos:
👉 [OPENCLAW_TOOLS.md](OPENCLAW_TOOLS.md)

---
© 2026 Que Vino!? - Configurado bajo la Constitución v1.5.2.
