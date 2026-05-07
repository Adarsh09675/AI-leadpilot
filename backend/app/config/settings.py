from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # API Settings
    API_KEY: str = "aviara-secret"
    PROJECT_NAME: str = "AI-LeadPilot"
    VERSION: str = "1.0.0"
    
    # Database Settings
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/leadpilot"
    
    # AI Settings
    GEMINI_API_KEY: Optional[str] = None
    
    # Slack Settings
    SLACK_WEBHOOK_URL: Optional[str] = None
    
    # Server Settings
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    model_config = SettingsConfigDict(env_file="backend/.env", extra="ignore")

settings = Settings()
