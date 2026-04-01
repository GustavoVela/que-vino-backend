# Data Model: Gestión de Base de Conocimiento RAG (Knowledge Stores)

Este documento define las entidades y estructuras de datos para el sistema de Knowledge Stores, alineadas con BigQuery y las APIs de Google GenAI.

## Entidades de Negocio

### 1. User
Representa a un administrador autenticado que interactúa con las APIs.
- **id**: (STRING) UID de Firebase.
- **email**: (STRING) Correo principal.
- **display_name**: (STRING) Nombre a mostrar.
- **email_verified**: (BOOLEAN) Estado de verificación.
- **photo_url**: (STRING, Opcional) Imagen de perfil.
- **phone_number**: (STRING, Opcional).
- **provider_id**: (STRING, Opcional).

### 2. Knowledge Store
Representa un repositorio de conocimiento en Gemini, espejado de un bucket de GCS.
- **store_id**: (STRING) ID único generado por Gemini `fileSearchStores/XYZ`.
- **display_name**: (STRING) Corresponde al `bucket_name` facilitado.
- **create_time**: (TIMESTAMP) Fecha de creación.
- **update_time**: (TIMESTAMP) Fecha de última modificación.

### 3. Knowledge Document
Representa un archivo individual indexado en un store.
- **file_id**: (STRING) ID único generado por Gemini `fileSearchStores/XYZ/documents/ABC`.
- **display_name**: (STRING) Nombre original en GCS (`original_filename`).
- **metadata**: (JSON) Contiene:
    - `bucket_name`: Origen del archivo.
    - `exact_size_bytes`: Tamaño en bytes para comparación.
    - `upload_date`: Fecha de sincronización.

## Esquemas de BigQuery (Auditoría)

### Tabla: `src_database.users`
| Columna | Tipo | Partición | Cluster |
| :--- | :--- | :--- | :--- |
| id | STRING | - | - |
| email | STRING | - | x |
| email_verified | BOOLEAN | - | x |
| display_name | STRING | - | - |
| photo_url | STRING | - | - |
| phone_number | STRING | - | - |
| provider_id | STRING | - | x |
| created_at | TIMESTAMP | x (Día) | - |
| updated_at | TIMESTAMP | - | - |

### Tabla: `src_api_transactions.authentication_log`
| Columna | Tipo | Partición | Cluster |
| :--- | :--- | :--- | :--- |
| transaction_id | STRING | - | - |
| user_id | STRING | - | x |
| email | STRING | - | x |
| status | STRING | - | x |
| error_message | STRING | - | - |
| event_timestamp | TIMESTAMP | x (Día) | - |
| ingestion_timestamp | TIMESTAMP | - | - |

### Tabla: `src_api_transactions.knowledge_store_api_log`
| Columna | Tipo | Partición | Cluster |
| :--- | :--- | :--- | :--- |
| transaction_id | STRING | - | - |
| bucket_name | STRING | - | x |
| store_id_gemini | STRING | - | - |
| performed_by_user_id | STRING | - | - |
| transaction_api_type | STRING | - | x |
| transaction_db_type | STRING | - | x |
| event_timestamp | TIMESTAMP | x (Día) | - |
| ingestion_timestamp | TIMESTAMP | - | - |

### Tabla: `src_api_transactions.knowledge_document_sync_log`
| Columna | Tipo | Partición | Cluster |
| :--- | :--- | :--- | :--- |
| transaction_id | STRING | - | - |
| bucket_name | STRING | - | x |
| store_id_gemini | STRING | - | x |
| file_name | STRING | - | - |
| action_taken | STRING | - | x |
| file_size_bytes | INT64 | - | - |
| performed_by_user_id | STRING | - | - |
| event_timestamp | TIMESTAMP | x (Día) | - |
| ingestion_timestamp | TIMESTAMP | - | - |

## Relaciones
- **User (1:N) Audit Logs**: Un usuario puede generar múltiples entradas en los logs de auditoría.
- **Knowledge Store (1:N) Knowledge Document**: Un repositorio contiene múltiples documentos indexados.
- **GCS Bucket (1:1) Knowledge Store**: Un repositorio se sincroniza con un único bucket fuente.
