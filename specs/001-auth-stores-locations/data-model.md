# Data Model & BigQuery Schematics

Las siguientes entidades y relaciones se mapean **exclusivamente a Google BigQuery**. Este documento conserva el 100% del rigor técnico (tipos, nulos, clustering y particionamiento) requerido para su ingesta.

### **1. Tabla: src_database.users (Usuarios Autenticados)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | REQUIRED | UID de Firebase (Primary Key). |
| email | STRING | REQUIRED | Correo electrónico principal del usuario. |
| email_verified | BOOLEAN | REQUIRED | Indica si el correo ha sido verificado en el proveedor. |
| display_name | STRING | REQUIRED | Nombre a mostrar del usuario. |
| photo_url | STRING | NULLABLE | URL de la foto de perfil (provista por Google/Firebase). |
| phone_number | STRING | NULLABLE | Número de teléfono asociado a la cuenta. |
| provider_id | STRING | NULLABLE | Proveedor de identidad. |
| created_at | TIMESTAMP | REQUIRED | Momento de creación en nuestra base de datos. |
| updated_at | TIMESTAMP | REQUIRED | Última vez que el usuario inició sesión o actualizó su token. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `provider_id`, `email_verified`

---

### **2. Tabla: src_api_transactions.authentication_log (Log de Autenticación)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | REQUIRED | Generado como UUID4 por backend |
| user_id | STRING | NULLABLE | Firebase UID |
| email | STRING | REQUIRED | Correo de intento |
| status | STRING | REQUIRED | SUCCESS, FAILED |
| error_message | STRING | NULLABLE | Opcional |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC) |
| ingestion_timestamp | TIMESTAMP | REQUIRED | Momento de escritura en BigQuery (DEFAULT CURRENT_TIMESTAMP()) |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `status`, `email`, `user_id`

---

### **3. Dataset: src_database.stores (Catálogo de tiendas principal)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | PRIMARY KEY | N/A (Generado como UUID4 por backend). |
| name | STRING | REQUIRED | Nombre de la Tienda |
| type | STRING | NULLABLE | Tipo (Digital, Mixta, Fisica) |
| digital_platform | STRING | NULLABLE | Plataforma (ej. Shopify) |
| is_producer | BOOLEAN | REQUIRED | ¿Productor? |
| has_wine_club | BOOLEAN | REQUIRED | ¿Tiene club de vino? |
| representative_name | STRING | NULLABLE | Representante |
| country_code | STRING | REQUIRED | Código de País (ej. MX, CO, US) |
| country_name | STRING | REQUIRED | Nombre del País |
| state_code | STRING | NULLABLE | Abreviatura del Estado |
| state_name | STRING | NULLABLE | Nombre del Estado |
| city_code | STRING | REQUIRED | Abreviatura de la Ciudad |
| city_name | STRING | REQUIRED | Nombre de la Ciudad |
| address | STRING | NULLABLE | Domicilio |
| contact_email | STRING | NULLABLE | Correo Electrónico |
| contact_phone | STRING | NULLABLE | Teléfono |
| website_url | STRING | NULLABLE | URL (Ej. https://www.cavasautto.com/) |
| social_media | JSON | NULLABLE | Formato JSON para agrupar redes (Instagram, Facebook, etc). |
| description | STRING | NULLABLE | Descripción Larga |
| created_at | TIMESTAMP | REQUIRED | Timestamp de Inserción. |
| updated_at | TIMESTAMP | REQUIRED | Timestamp de Actualización. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `type`, `country_code`, `state_code`, `city_code`

---

### **4. Tabla: src_api_transactions.stores_log (Auditoría CRUD Tiendas)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware. |
| performed_by_user_id | STRING | NULLABLE | UID de Firebase. |
| performed_by_email | STRING | NULLABLE | Correo electrónico extraído del JWT. |
| transaction_api_type | STRING | CLUSTER KEY | 'GET', 'POST', 'PUT', 'DELETE'. |
| transaction_api_path | STRING | CLUSTER KEY | Path relativo HTTP invocado. |
| transaction_db_type | STRING | CLUSTER KEY | 'INSERT', 'UPDATE', 'DELETE', 'SELECT'. |
| transaction_parameters | JSON | NULLABLE | Parámetros de la consulta/mutación. |
| payload_before | JSON | NULLABLE | Snapshot del registro *antes* de la mutación. |
| payload_after | JSON | NULLABLE | Snapshot del registro *después* de la mutación. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución en el servidor (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `transaction_api_type`, `transaction_api_path`, `transaction_db_type`, `performed_by_user_id`

---

### **5. Dataset: src_database.locations (Catálogo de localizaciones)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| id | STRING | PRIMARY KEY | UUID v4 generado por el backend. |
| country_code | STRING | REQUIRED | Código ISO Alpha-2 (ej. 'MX'). Exactamente 2 caracteres. |
| country_name | STRING | REQUIRED | Nombre comercial (ej. 'México'). |
| state_code | STRING | NULLABLE | Estado o Provincia (ej. 'NAR'). |
| state_name | STRING | NULLABLE | Nombre del Estado o Provincia (ej. 'Nariño'). |
| city_code | STRING | REQUIRED | Abreviatura (ej. 'GDL', 'CDMX'). |
| city_name | STRING | REQUIRED | Nombre de la Ciudad. |
| created_at | TIMESTAMP | REQUIRED | Momento de creación. |
| updated_at | TIMESTAMP | REQUIRED | Momento de la última modificación. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `created_at` (por día)
* **Clusterización:** `id`, `country_code`, `state_code`, `city_code`

---

### **6. Tabla: src_api_transactions.locations_log (Auditoría CRUD Localizaciones)**

| Nombre de Columna | Tipo de Dato | Restricción | Descripción |
| :---- | :---- | :---- | :---- |
| transaction_id | STRING | PRIMARY KEY | UUID v4 generado por el middleware. |
| performed_by_user_id | STRING | NULLABLE | UID de Firebase. |
| performed_by_email | STRING | NULLABLE | Correo extraído del JWT. |
| transaction_api_type | STRING | CLUSTER KEY | 'GET', 'POST', 'PUT', 'DELETE'. |
| transaction_api_path | STRING | CLUSTER KEY | Path relativo HTTP invocado. |
| transaction_db_type | STRING | CLUSTER KEY | 'INSERT', 'UPDATE', 'DELETE', 'SELECT'. |
| transaction_parameters | JSON | NULLABLE | Parámetros de la transacción. |
| payload_before | JSON | NULLABLE | Snapshot antes de la mutación. |
| payload_after | JSON | NULLABLE | Snapshot después de la mutación. |
| event_timestamp | TIMESTAMP | REQUIRED | Momento exacto de ejecución (UTC). |
| ingestion_timestamp | TIMESTAMP | PARTITION KEY | Momento de escritura en BigQuery. |

**Configuración de Optimización (BigQuery):**
* **Particionamiento:** `event_timestamp` (por día)
* **Clusterización:** `transaction_api_type`, `transaction_api_path`, `transaction_db_type`, `performed_by_user_id`
