from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXP_MINUTES: int
    DATABASE_URI: str


settings = Settings() # type: ignore[call-arg]