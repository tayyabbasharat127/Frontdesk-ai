from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    redis_url: str = "redis://localhost:6379/0"
    llm_model: str = "gpt-4.1-mini"
    embedding_model: str = "text-embedding-3-small"
    vapi_secret: str = ""
    whatsapp_verify_token: str = ""
    whatsapp_token: str = ""
    whatsapp_app_secret: str = ""
    nexhealth_api_key: str = ""
    nexhealth_base_url: str = "https://nexhealth.info"
    jwt_secret: str = "dev"
    slot_step_minutes: int = 15


@lru_cache
def get_settings() -> Settings:
    return Settings()