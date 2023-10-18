from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Config(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRY_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Config()
