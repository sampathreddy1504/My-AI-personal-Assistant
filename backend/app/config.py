# backend/app/config.py

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    ✅ Central configuration for Personal AI Assistant
    Works seamlessly on Render (FastAPI + Celery + Redis + PostgreSQL + Neo4j)
    """

    # ======================================================
    # 🔹 Application
    # ======================================================
    APP_NAME: str = Field("Personal AI Assistant", env="APP_NAME")
    ENVIRONMENT: str = Field("production", env="ENVIRONMENT")
    DEBUG: bool = Field(False, env="DEBUG")
    PORT: int = Field(8000, env="PORT")
    HOST: str = Field("0.0.0.0", env="HOST")

    # ======================================================
    # 🔹 PostgreSQL Database
    # ======================================================
    POSTGRES_USER: str = Field("postgres", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("postgres", env="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("personal_ai", env="POSTGRES_DB")
    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")

    @property
    def DATABASE_URL(self) -> str:
        """✅ Unified PostgreSQL connection string"""
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # ======================================================
    # 🔹 Redis (used by memory, Celery, and chat subsystems)
    # ======================================================
    # Default Redis URL (Render-provided Upstash or local)
    REDIS_URL: str = Field("redis://localhost:6379/0", env="REDIS_URL")

    # Optional custom channels for subsystems
    REDIS_URL_CELERY: str = Field("redis://localhost:6379/0", env="REDIS_URL_CELERY")
    REDIS_URL_CHAT: str = Field("redis://localhost:6379/1", env="REDIS_URL_CHAT")
    REDIS_CHAT_HISTORY_KEY: str = Field("chat_history", env="REDIS_CHAT_HISTORY_KEY")

    # ======================================================
    # 🔹 Celery Task Queue
    # ======================================================
    CELERY_BROKER_URL: str = Field(..., env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = Field(..., env="CELERY_RESULT_BACKEND")

    # ======================================================
    # 🔹 Neo4j Graph Database
    # ======================================================
    NEO4J_URI: str = Field("bolt://localhost:7687", env="NEO4J_URI")
    NEO4J_USER: str = Field("neo4j", env="NEO4J_USER")
    NEO4J_PASSWORD: str = Field("password", env="NEO4J_PASSWORD")

    # ======================================================
    # 🔹 AI Keys and Models
    # ======================================================
    GEMINI_API_KEYS: str = Field(..., env="GEMINI_API_KEYS")  # Comma-separated keys
    GEMINI_MODEL: str = Field("gemini-2.0-flash", env="GEMINI_MODEL")
    COHERE_API_KEY: Optional[str] = Field(None, env="COHERE_API_KEY")

    # ======================================================
    # 🔹 Google OAuth / Email (optional)
    # ======================================================
    GOOGLE_CLIENT_ID: Optional[str] = Field(None, env="GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: Optional[str] = Field(None, env="GOOGLE_CLIENT_SECRET")
    EMAIL_USER: Optional[str] = Field(None, env="EMAIL_USER")
    EMAIL_PASS: Optional[str] = Field(None, env="EMAIL_PASS")

    # ======================================================
    # 🔹 Auth / Security
    # ======================================================
    JWT_SECRET_KEY: str = Field("change_me_in_env", env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    JWT_EXPIRES_MINUTES: int = Field(60 * 24 * 7, env="JWT_EXPIRES_MINUTES")  # 7 days

    # ======================================================
    # 🔹 AI Config
    # ======================================================
    AI_PROVIDER_FAILURE_TIMEOUT: int = Field(30, env="AI_PROVIDER_FAILURE_TIMEOUT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # ✅ safely ignore any unexpected vars


# ======================================================
# ✅ Global settings instance (used everywhere)
# ======================================================
settings = Settings()
