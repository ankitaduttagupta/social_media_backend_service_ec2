from fastapi import FastAPI
from app.api.routes import router as media_router

app = FastAPI()
app.include_router(media_router, prefix="/media")