from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Logistics Data Simulator API"
    DATABASE_URL: str = "sqlite+aiosqlite:///./data.db"
    API_KEY: str = "SECRET_API_KEY"
    REQUIRE_API_KEY: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
