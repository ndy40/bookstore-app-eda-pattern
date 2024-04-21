import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = Path(__file__).parent.parent.parent / '.env'


class AppConfig(BaseSettings):
    APP_ENV: str = "development"
    DB_NAME: str = "bookstore"
    DB_URL: str

    model_config = SettingsConfigDict(env_file=env_path)


config = AppConfig()
