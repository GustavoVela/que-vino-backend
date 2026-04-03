# Que Vino!? OPENCLAW API Inventory (v2.2)

Este documento es el catálogo unificado de herramientas productivas para agentes de IA en el ecosistema **Que Vino!?**. Define los endpoints, esquemas de entrada y comportamiento esperado para cada micro-swarm.

---

## 🔒 Estándar de Autenticación

Todas las peticiones (excepto `/health`) deben incluir un **Bearer Token (Firebase ID Token)** en el header `Authorization`.

**URL para obtención de Token**:
```
POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[FIREBASE_API_KEY]
Body: {"email": "...", "password": "...", "returnSecureToken": true}
```

---

## 🔒 Estándar de CORS

Los microservicios aceptan peticiones desde los siguientes orígenes autorizados:
- `http://localhost`, `http://localhost:3000`, `http://localhost:5173`
- `https://quevino.mx`, `https://www.quevino.mx`
- `https://que-vino-admin.lovable.app`
- `https://9ebf32fb-b85f-43d4-b440-af3007c90f34.lovableproject.com`
- `https://id-preview--9ebf32fb-b85f-43d4-b440-af3007c90f34.lovable.app`

---

## 🏪 1. Stores API (Tiendas y Marcas)

Gestión centralizada de tiendas, productores y clubes de vino.

- **URL Producción**: `https://quevino-stores-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/stores/`
- **Uso**: Listar y buscar marcas de vino y entidades comerciales.

---

## 📍 2. Locations API (Sucursales)

Catálogo de puntos de venta físicos, geolocalización y horarios.

- **URL Producción**: `https://quevino-locations-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/locations/`
- **Uso**: Localizar tiendas físicas cercanas al usuario.

---

## 🧠 3. Knowledge Stores API (RAG System)

Gestión de bases de conocimiento nativas en Gemini (File Search). Permite el mirroring automático entre Google Cloud Storage y el motor de búsqueda semántica de Gemini.

- **URL Producción**: `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/knowledge_stores/`
- **MCP Server**: `apis/knowledge_stores/mcp_server.py`
- **Test Results**: `apis/knowledge_stores/tests/TEST_RESULTS.md`

### 3.1 Health Check (público)
- `GET /health` → `{"status": "ok", "environment": "dev"}`

### 3.2 Listar Stores
- `GET /knowledge-stores`
- **Requiere**: `Authorization: Bearer <token>`
- **Respuesta**: Array de `{"id": "fileSearchStores/{short_id}", "display_name": "..."}`

### 3.3 Listar Documentos de un Store
- `GET /knowledge-stores/{store_id}/files`
- **Nota**: Acepta el ID corto (ej: `grapes-bpdsyaih31jh`) o el nombre completo.
- **Respuesta**: Array de `{"id": "...", "display_name": "...", "metadata": {}}`

### 3.4 Sincronización GCS → Gemini
- `POST /knowledge-stores/sync`
- **Body**: `{"bucket_name": "...", "prefix": "...", "store_name": "..."}`
- **Respuesta**: `{"status": "completed", "transaction_id": "...", "summary": {"uploaded": N, "skipped": N, "deleted": N, "errors": N}}`

### 3.5 Eliminar Store
- `DELETE /knowledge-stores/{store_id}` → `204 No Content`

### 3.6 Eliminar Documento
- `DELETE /knowledge-stores/{store_id}/files/{file_id}` → `204 No Content`

---

## 🔊 4. Audio Generation API (TTS)

Servicio unificado de síntesis de voz (TTS) con enriquecimiento emocional mediante IA (Gemini).

- **URL Producción**: `https://quevino-audio-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/audio/`
- **MCP Server**: `apis/audio/mcp_server.py`
- **Test Results**: `apis/audio/tests/TEST_RESULTS.md`

### 4.1 Health Check (público)
- `GET /health` → `{"status": "ok", "service": "que-vino-audio-api"}`

### 4.2 Catálogo de Voces
- `GET /audio/providers/voices`
- **Requiere**: `Authorization: Bearer <token>`
- **Respuesta**: Array de voces unificadas de ElevenLabs y Google.
  ```json
  [
    {"provider": "ELEVENLABS", "voice_id": "kh59ZgGFT1YQNe4P0U2V", "name": "Rachel", ...},
    {"provider": "GOOGLE", "voice_id": "es-US-Neural2-A", "ssml_gender": "FEMALE", ...}
  ]
  ```

### 4.3 Catálogo de Modelos
- `GET /audio/providers/models`
- **Requiere**: `Authorization: Bearer <token>`
- **Respuesta**: Lista de modelos disponibles por proveedor.

### 4.4 Generación de Audio
- `POST /audio/generate`
- **Requiere**: `Authorization: Bearer <token>`
- **Body**:
  ```json
  {
    "text": "Tu texto aquí...",
    "provider": "ELEVENLABS",
    "voice_id": "kh59ZgGFT1YQNe4P0U2V",
    "model_id": "eleven_multilingual_v2",
    "output_format": "mp3",
    "enrich_audio": false
  }
  ```
- **Campos**:
  - `text` ✅ requerido — Texto a sintetizar.
  - `provider` ✅ requerido — `ELEVENLABS` o `GOOGLE`.
  - `voice_id` ✅ requerido — ID de la voz (del catálogo `GET /audio/providers/voices`).
  - `model_id` ❌ opcional — Modelo de síntesis (ej: `eleven_multilingual_v2`, `eleven_v3`).
  - `output_format` ❌ opcional — `mp3` (defecto) o `wav`.
  - `enrich_audio` ❌ opcional — Enriquecimiento emocional con Gemini.
- **Respuesta (201)**: Byte stream binario (`audio/mpeg` o `audio/wav`).
- **Headers de trazabilidad**: `X-Generation-ID`, `X-Enrichment-Status`.

---

## 📜 Definición de Hecho (DoD) para Agentes

1. **Auditoría**: Cada transacción POST/DELETE es logueada en BigQuery (`src_api_transactions`).
2. **Resiliencia**: Ante errores 401, solicitar un token nuevo antes de reintentar.
3. **Concurrencia**: El mirroring de Knowledge Stores soporta hasta 10 hilos paralelos.
4. **Pruebas**: Cada microservicio tiene `tests/test_production.py` y `tests/TEST_RESULTS.md` actualizados.

---
© 2026 Que Vino!? — Constitución v1.5.2 | Agentic Architecture.
