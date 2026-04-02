# Que Vino OPENCLAW API Inventory

Este documento rastrea todas las APIs y agentes productivos expuestos en el ecosistema `que-vino-backend`. Es la fuente de verdad para que los agentes de IA descubran y utilicen herramientas.

## APIs de Negocio

### 1. Stores API (Gestión de Tiendas)
- **URL Producción**: `https://quevino-stores-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/stores/`
- **Uso**: Gestión centralizada de marcas y entidades legales de tiendas.

#### 1.1 Listar Tiendas
- **GET** `/stores`
- **Params**: `limit`, `offset`
- **Ejemplo**: `curl -H "Authorization: Bearer <TOKEN>" "https://quevino-stores-2lkhisz2aa-uc.a.run.app/stores"`

#### 1.2 Búsqueda Semántica/Nombre
- **GET** `/stores/search`
- **Params**: `name` (Requerido)
- **Ejemplo**: `curl -H "Authorization: Bearer <TOKEN>" "https://quevino-stores-2lkhisz2aa-uc.a.run.app/stores/search?name=Vinoteca"`

---

### 2. Locations API (Gestión de Sucursales)
- **URL Producción**: `https://quevino-locations-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/locations/`
- **Uso**: Gestión de puntos de venta físicos, geolocalización y horarios.

#### 2.1 Listar Sucursales
- **GET** `/locations`
- **Ejemplo**: `curl -H "Authorization: Bearer <TOKEN>" "https://quevino-locations-2lkhisz2aa-uc.a.run.app/locations"`

#### 2.2 Crear Sucursal
- **POST** `/locations`
- **Body**: `{"name": "...", "store_id": "...", "latitude": ..., "longitude": ...}`

---

### 3. Knowledge Stores API (RAG & IA)
- **URL Producción**: `https://quevino-knowledge-stores-2lkhisz2aa-uc.a.run.app`
- **Repositorio**: `apis/knowledge_stores/`
- **SDK**: **Gemini GenAI Native (v1.70.0+)**
- **Uso**: Sincronización de bases de conocimiento desde GCS hacia Gemini para búsqueda semántica.

#### 3.1 Sincronizar Base de Conocimiento (Mirroring)
- **POST** `/sync-bucket`
- **Body**: `{"bucket_name": "...", "store_name": "...", "user_id": "..."}`
- **Descripción**: Realiza un mirroring paralelo (Semaphore 10) entre GCS y Gemini.

#### 3.2 Listar Repositorios de IA
- **GET** `/stores`
- **Descripción**: Lista los *File Search Stores* activos en Gemini.

---

### 4. Audio Generation API (TTS)
- **Repositorio**: `apis/audio/`
- **MCP Server**: `apis/audio/mcp_server.py`
- **Uso**: Generación de audio (Text-to-Speech) con enriquecimiento emocional vía Gemini.
- **Proveedores**: ElevenLabs (High Fidelity) y Google Cloud TTS (Technical/Standard).

#### 4.1 Generar Audio (Stream)
- **POST** `/audio/generate`
- **Body**: `{"text": "Hola mundo", "provider": "ELEVENLABS", "voice_id": "rachel", "enrich_audio": true}`
- **Respuesta**: Byte Stream (MP3/WAV) + Headers `X-Generation-ID`.

#### 4.2 Listar Voces Unidas
- **GET** `/audio/providers/voices`
- **Descripción**: Expone voces de ElevenLabs y Google mapeadas a un esquema común.

---

## 🛠️ Token de Prueba (Temporal)
Para visualización completa de respuestas, usa el siguiente token (válido por 1 hora desde 2026-04-01 11:40 AM):
`[GCLOUD_TOKEN_HERE]`

---

## 📜 Definición de Hecho (DoD) para Agentes
Los agentes que operen estas herramientas deben:
1. Validar siempre el código de respuesta HTTP.
2. Manejar errores 401 (Token expirado) solicitando refresco.
3. Consultar los esquemas de BigQuery en `/schemas/` de cada API para entender la estructura de datos extendida.
