from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Card Ranker"
    model_config = SettingsConfigDict(env_file=".env")


@cache
def get_settings():
    return Settings()
