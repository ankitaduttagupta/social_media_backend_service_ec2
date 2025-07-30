from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.services.media import upload_file
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services.media import get_media_by_user
import shutil
from app.utils.s3_utils import upload_file_to_s3

router = APIRouter()

@router.post("/upload_file")
async def upload_file(
    file: UploadFile = File(...),
    user_id: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    return await upload_file(file, user_id, db)

@router.get("/user/{user_id}")
async def get_user_media(user_id: str, db: AsyncSession = Depends(get_db)):
    from app.services.media import get_media_by_user
    return await get_media_by_user(user_id, db)


@router.post("/upload_media")
async def upload_file(file: UploadFile = File(...)):
    temp_file_path = f"/tmp/{file.filename}"

    # Save file temporarily
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Upload to S3
    url = upload_file_to_s3(temp_file_path, f"media/{file.filename}")

    return {"message": "Uploaded successfully", "url": url}
