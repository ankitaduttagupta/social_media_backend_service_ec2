import asyncio
from fastapi import FastAPI
from app.api.routes import router as feed_router
from app.consumers.media_consumer import consume_media_uploaded

app = FastAPI()
app.include_router(feed_router, prefix="/feed")

@app.on_event("startup")
async def start_consumer():
    asyncio.create_task(consume_media_uploaded())
