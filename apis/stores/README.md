# Que Vino!? Stores API

Microservicio y herramienta MCP para la indexación y búsqueda de tiendas, productores y clubes de vino. Expone tanto endpoints REST como herramientas de MCP para que los agentes inteligentes puedan consultar información sobre tiendas directamente.

## 🚀 Arquitectura Local

```bash
cd apis/stores
poetry install
poetry run uvicorn main:app --reload --port 8080
```

## 🛠️ MCP Toolset (Model Context Protocol)

Este servicio puede ser cargado como un servidor MCP para que IAs como Claude o Gemini puedan buscar tiendas:

```bash
cd apis/stores
poetry run mcp dev mcp_server.py
```

## 📦 Despliegue en Google Cloud

Utiliza Cloud Build para crear la imagen de Docker y desplegarla en Cloud Run.

```bash
gcloud builds submit --config apis/stores/deploy/cloudbuild.yaml .
```

La configuración por defecto es **max-instances=1** para controlar costes y escalado seguro en fases iniciales.

## 🔒 Seguridad
- **Auth**: Valida `Authorization: Bearer <ID_TOKEN>` de Firebase.
- **Auditoría**: Todas las mutaciones (POST/PUT/DELETE) se registran en `src_api_transactions.stores_log`.

---
© 2026 Que Vino!? - Cloud Run Managed Micro-Swarms
