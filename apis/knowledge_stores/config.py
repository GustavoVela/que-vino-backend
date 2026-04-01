from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Configuración global del entorno para Knowledge Stores.
    """
    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding='utf-8', extra='ignore')
    
    project_id: str = "que-vino-23032025"
    environment: str = "dev"
    
    # Dataset names according to constitution
    bq_dataset_database: str = "src_database"
    bq_dataset_transactions: str = "src_api_transactions"
    
    # Tables
    table_users: str = "users"
    table_auth_log: str = "authentication_log"
    table_store_api_log: str = "knowledge_store_api_log"
    table_sync_log: str = "knowledge_document_sync_log"
    
    # Gemini API Key (Optional if using ADC/Cloud Run identity)
    # Map from GEMINI_FILE_SEARCH_API_KEY or FIREBASE_API_KEY in .env
    gemini_file_search_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    firebase_api_key: Optional[str] = None
    
    # Firebase Auth
    firebase_project_id: str = "que-vino-23032025"

    @property
    def effective_google_api_key(self) -> Optional[str]:
        return self.gemini_file_search_api_key or self.google_api_key or self.firebase_api_key

settings = Settings()
