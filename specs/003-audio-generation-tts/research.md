# Research Findings: Generación de Audio Multi-Proveedor (TTS API)

**Feature**: `003-audio-generation-tts`
**Status**: Resolved

## Unknowns & Clarifications

### Research Item 1: ElevenLabs Audio Tags vs Google SSML
- **Decision**: Gemini actuará como "Director de Orquesta" diferenciado por proveedor.
    - **ElevenLabs (v3)**: Se utilizarán **Audio Tags** propios entre corchetes (ej. `[whispers]`, `[laughs]`, `[pause]`). **IMPORTANTE**: No usar SSML `<break>` con Eleven v3.
    - **Google TTS**: Se utilizará **SSML (Speech Synthesis Markup Language)** estándar (ej. `<emphasis>`, `<prosody>`, `<break time="1s"/>`) para controlar tono y velocidad.
- **Rationale**: ElevenLabs v3 está optimizado para interpretar cues emocionales en texto plano, mientras que Google TTS ofrece un control técnico preciso mediante SSML.
- **Alternatives Considered**: Usar un solo marcado universal. Rechazado porque degradaría la calidad de ElevenLabs (SSML ignorado) o de Google (tags de corchetes leídos como texto literal).

### Research Item 2: Latencia y Caché de Voces
- **Decision**: Implementar un caché en memoria con TTL de 24 horas para los catálogos de voces.
- **Rationale**: El catálogo de ElevenLabs y Google no cambia con frecuencia intradía. Consultas directas añaden ~400ms de latencia innecesaria.
- **Alternatives Considered**: Cachear en BigQuery. Rechazado por complejidad innecesaria para un JSON pequeño (< 500kb).

### Research Item 3: IAM Minimalista (GCS Audit)
- **Decision**: Asignar el rol `roles/storage.objectCreator` al Service Account del microservicio sobre el bucket `que-vino-23032025-audios`.
- **Rationale**: Permite crear objetos (escritura) pero no borrarlos ni listarlos públicamente, cumpliendo con la política de auditoría inmutable de la Constitución.
- **Alternatives Considered**: `roles/storage.objectAdmin`. Rechazado por violar el principio de menor privilegio (específicamente la inmutabilidad).

## Best Practices & Patterns

### 1. Unified Provider Interface (Strategy Pattern)
- Implementar una clase base `TTSProvider` con métodos abstractos `synthesize` y `list_voices`.
- Esto permite añadir proveedores futuros (ej. Azure o OpenAI) sin cambiar la lógica del servicio principal.

### 2. Transactional Integrity
- La respuesta al cliente DEBE incluir el `generation_id` (UUID).
- Si la escritura en GCS falla tras 3 reintentos, el audio se descarta y se responde con ERROR 500, asegurando que no existan inconsistencias entre "Audio entregado" y "Audio auditado".

### 3. Gemini System Prompts (Diferenciados)

#### Prompt para ElevenLabs (Cues Emocionales)
- "Eres un experto en dirección vocal para actores de ElevenLabs. Tu misión es inyectar pausas y tonos emocionales usando etiquetas entre corchetes `[tag]`. Ejemplos válidos: `[laughs]`, `[whispers]`, `[pause]`, `[excited]`, `[sighs]`. No uses SSML. Devuelve ÚNICAMENTE el texto con las etiquetas integradas de forma natural."

#### Prompt para Google TTS (SSML Técnico)
- "Eres un experto en SSML para Google Cloud TTS. Tu misión es envolver el texto en etiquetas `<speak>` e inyectar `<emphasis>`, `<prosody rate='slow'>`, y `<break time='500ms'/>` para que la lectura sea profesional y clara. Devuelve el XML SSML completo."
