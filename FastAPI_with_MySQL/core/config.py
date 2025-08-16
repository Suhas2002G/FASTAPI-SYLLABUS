# config.py

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App Info
    PROJECT_NAME: str = "FastAPI App"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Production-ready FastAPI application"

    # Environment
    ENVIRONMENT: str = "development"  # development | staging | production
    DEBUG: bool = True

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/dbname"

    # Security
    SECRET_KEY: str = "CHANGE_ME"  # use secrets.token_urlsafe(32) in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    Ensures settings are loaded once and reused across the app.
    """
    return Settings()



# Pydantic BaseSettings → Automatically loads variables from .env or system environment.

# @lru_cache → Prevents reloading settings multiple times when injected into dependencies.

# Multiple Environments → Supports development, staging, and production.

# Security Defaults → SECRET_KEY, JWT ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES.

# Database Config → Uses async connection string (asyncpg for Postgres).

# CORS Support → Defined origins list for frontend integration.

# Logging Level → Configurable (DEBUG, INFO, etc.).