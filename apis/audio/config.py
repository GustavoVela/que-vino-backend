import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "que-vino-audio-api"
    environment: str = "dev"
    PORT: int = 8080

    # Project Settings
    project_id: str = os.getenv("PROJECT_ID", "que-vino-23032025")
    region: str = "us-central1"

    # API Keys (Reflecting Audio-specific variables)
    GEMINI_AUDIO_API_KEY: Optional[str] = os.getenv("GEMINI_AUDIO_API_KEY")
    ELEVENLABS_AUDIO_API_KEY: Optional[str] = os.getenv("ELEVENLABS_AUDIO_API_KEY")
    GEMINI_AUDIO_MODEL: str = os.getenv("GEMINI_AUDIO_MODEL", "gemini-2.5-flash")

    # Voces por Defecto (Sección 3.1 de la Constitución)
    DEFAULT_VOICE_ELEVENLABS: str = os.getenv("DEFAULT_VOICE_ELEVENLABS", "21m00Tcm4TDOqjz76jtA") # Rachel
    DEFAULT_VOICE_GOOGLE: str = os.getenv("DEFAULT_VOICE_GOOGLE", "es-US-Neural2-A")

    # Cloud Storage (Media Centralizada - Sección 2.6 de la Constitución)
    GCS_AUDIO_BUCKET_NAME: str = os.getenv("GCS_AUDIO_BUCKET_NAME", "que-vino-23032025-media")
    GCS_AUDIO_FOLDER: str = "audio"

    # BQ Datasets (Standard defined by constitution)
    bq_dataset_database: str = "src_database"
    bq_dataset_transactions: str = "src_api_transactions"

    # Tables
    table_users: str = "users"
    table_auth_log: str = "authentication_log"
    table_audio_api_log: str = "audio_api_log"
    table_audio_generation_log: str = "audio_generation_log"

    # Firebase Auth (Identity)
    FIREBASE_PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID", "que-vino-23032025")

    model_config = SettingsConfigDict(
        env_file="../../.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
