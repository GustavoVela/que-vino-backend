# Que Vino!? OPENCLAW API Inventory (v2.1)

Este documento es el catálogo unificado de herramientas productivas para agentes de IA en el ecosistema **Que Vino!?**. Define los endpoints, esquemas de entrada y comportamiento esperado para cada micro-swarm.

---

## 🔒 Estándar de Autenticación
Todas las peticiones deben incluir un **Bearer Token (Firebase ID Token)** en el header `Authorization`.

**URL para obtención de Token (Auth API)**:
`POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[FIREBASE_API_KEY]`

---

## 🔒 Estándar de CORS
Los microservicios están configurados para aceptar únicamente peticiones desde los siguientes orígenes autorizados (sin comodines por seguridad):
- `http://localhost`, `http://localhost:3000`, `http://localhost:5173`
- `https://quevino.mx`, `https://www.quevino.mx`
- `https://que-vino-admin.lovable.app`
- `https://9ebf32fb-b85f-43d4-b440-af3007c90f34.lovableproject.com`
- `https://id-preview--9ebf32fb-b85f-43d4-b440-af3007c90f34.lovable.app`

---
Gestión centralizada de tiendas, productores y clubes de vino.

- **URL Producción**: `https://quevino-stores-2lkhisz2aa-uc.a.run.app`
- **Uso**: Listar y buscar marcas de vino y entidades comerciales.

---

## 📍 2. Locations API (Sucursales)
Catálogo de puntos de venta físicos, geolocalización y horarios.

- **URL Producción**: `https://quevino-locations-2lkhisz2aa-uc.a.run.app`
- **Uso**: Localizar tiendas físicas cercanas al usuario.

---

## 🧠 3. Knowledge Stores API (RAG System)
Gestión de bases de conocimiento nativas en Gemini (File Search). Permite el 'mirroring' automático entre Google Cloud Storage y el motor de búsqueda semántica.

- **URL Producción**: `https://quevino-knowledge-stores-678275032484.us-central1.run.app`
- **Repositorio**: `apis/knowledge_stores/`
- **MCP Server**: `apis/knowledge_stores/mcp_server.py`

### 3.1 Sincronización Masiva (GCS -> Gemini)
- **POST** `/knowledge-stores/sync`
- **Body**: `{"bucket_name": "...", "prefix": "...", "store_name": "..."}`
- **Descripción**: Mirroring incremental con limpieza de huérfanos.

### 3.2 Listado de Stores
- **GET** `/knowledge-stores`
- **Respuesta**: Listado de IDs de recursos para grounding (ej: `fileSearchStores/{id}`).

---

## 🔊 4. Audio Generation API (TTS)
Servicio unificado de síntesis de voz con enriquecimiento emocional mediante IA.

- **URL Producción**: `https://quevino-audio-678275032484.us-central1.run.app`
- **Repositorio**: `apis/audio/`
- **MCP Server**: `apis/audio/mcp_server.py`

### 4.1 Generación de Audio (Multi-Provider)
- **POST** `/audio/generate`
- **Body Request**:
  ```json
  {
    "text": "Tu texto aquí...",
    "provider": "ELEVENLABS" | "GOOGLE",
    "voice_id": "rachel" | "es-US-Neural2-A",
    "output_format": "mp3" | "wav",
    "enrich_audio": true 
  }
  ```
- **Respuesta**: Byte Stream binario (Content-Type: audio/mpeg o audio/wav).
- **Headers**: `X-Generation-ID`, `X-Enrichment-Status`.

### 4.2 Catálogo de Voces
- **GET** `/audio/providers/voices`
- **Descripción**: Voces reconciliadas (GCP + ElevenLabs).

---

## 📜 Definición de Hecho (DoD) para Agentes
1. **Auditoría**: Cada transacción POST/DELETE es logueada en BigQuery.
2. **Resiliencia**: Manejo de 401 vía solicitud de nuevo token.
3. **Concurrencia**: Mirroring soporta 10 hilos paralelos.

---
© 2026 Que Vino!? - Constitución y Reglas de Agentic Architecture.
