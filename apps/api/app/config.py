from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Convexis"
    environment: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_name: str = "postgres"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_sslmode: str = "prefer"
    db_pool_size: int = 5
    db_max_overflow: int = 10
    app_data_dir: str = Field(default=str(Path("./.convexis-data").resolve()))

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            "postgresql+psycopg://"
            f"{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            f"?sslmode={self.db_sslmode}"
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
