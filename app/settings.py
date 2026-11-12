from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Card Ranker"
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache(maxsize=None)
def get_settings():
    return Settings()