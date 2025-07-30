import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    KAFKA_BOOTSTRAP_SERVERS: str
    JWT_SECRET_KEY: str = "super-secret"

    class Config:
        env_file = ".env"

settings = Settings()
