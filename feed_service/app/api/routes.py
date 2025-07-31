from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.feed import get_feed
from app.models.feed import Feed
from datetime import datetime
from app.schema.schemas import FeedCreateSchema
from app.utils.s3_utils import upload_file_to_s3
router = APIRouter()
#sample route to get user feed
@router.get("/{user_id}")
async def user_feed(user_id: str, db: AsyncSession = Depends(get_db)):
    return await get_feed(user_id, db)


@router.post("/feed/")
async def create_feed(
    payload: FeedCreateSchema,
    db: AsyncSession = Depends(get_db)
):
    feed = Feed(
        user_id= payload.user_id,
        media_id=payload.media_id,
        file_url=payload.file_url,
        created_at=datetime.utcnow()
    )
    db.add(feed)
    await db.commit()
    await db.refresh(feed)
    return {"Status": "created!", "data":feed}



@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_url = upload_file_to_s3(file.file, file.filename, file.content_type)
    return {"file_url": file_url}
