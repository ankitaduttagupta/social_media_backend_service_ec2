import os
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # load .env at startup


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET: str
    DATABASE_URL: str
    KAFKA_BOOTSTRAP_SERVERS: str

    class Config:
        env_file = ".env"

settings = Settings()