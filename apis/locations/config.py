from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuración global del entorno.
    """
    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding='utf-8', extra='ignore')
    
    project_id: str = "que-vino-23032025"
    environment: str = "dev"

settings = Settings()
