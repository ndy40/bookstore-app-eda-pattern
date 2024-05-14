import pkgutil
from functools import cache

from pydantic_settings import BaseSettings


@cache
def get_modules_path():
    return [f'bookstore.modules.{module.name}'
            for module in pkgutil.iter_modules(['bookstore/modules'])
            ]


class AppConfig(BaseSettings):
    APP_ENV: str = "development"
    DB_NAME: str = "app"
    DB_URL: str

    CELERY_RESULT_BACKEND: str
    BROKER_URL: str
    task_modules: list[str] = get_modules_path()
    API_PORT: int | None = 5000


config = AppConfig()
