from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    APP_ENV: str = "development"
    DB_NAME: str = "app"
    DB_URL: str

    CELERY_RESULT_BACKEND: str
    BROKER_URL: str
    task_modules: list[str] = [
        "bookstore.modules.book_mgt",
        "bookstore.modules.catalog",
    ]
    API_PORT: int | None = 5000


config = AppConfig()
