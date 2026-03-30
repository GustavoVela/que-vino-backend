# Que Vino!? Locations API

Microservicio y herramienta MCP para el catálogo de localizaciones (países, estados, ciudades) de Chile, Perú y otros mercados de interés.

## 🚀 Arquitectura Local

```bash
cd apis/locations
poetry install
poetry run uvicorn main:app --reload --port 8080
```

## 🛠️ MCP Toolset (Model Context Protocol)

Este servicio puede ser cargado como un servidor MCP para que IAs como Claude o Gemini puedan buscar localizaciones:

```bash
cd apis/locations
poetry run mcp dev mcp_server.py
```

## 📦 Despliegue en Google Cloud

Utiliza Cloud Build para crear la imagen de Docker y desplegarla en Cloud Run.

```bash
gcloud builds submit --config apis/locations/deploy/cloudbuild.yaml .
```

La configuración por defecto es **max-instances=1** para controlar costes y escalado seguro en fases iniciales.

## 🔒 Auditoría
Todas las mutaciones (POST/PUT/DELETE) se registran en `src_api_transactions.locations_log`.

---
© 2026 Que Vino!? - Cloud Run Managed Micro-Swarms
