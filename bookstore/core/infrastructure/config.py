from pydantic.v1 import BaseSettings


class AppConfig(BaseSettings):
    APP_ENV: str = "development"
    DB_NAME: str = "bookstore"
    DB_URL: str = "postgresql+psycopg2:"
