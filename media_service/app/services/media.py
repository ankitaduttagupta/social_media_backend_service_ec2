import boto3
import uuid
import os
from fastapi import UploadFile
from app.models.media import Media
from app.db.database import SessionLocal
from sqlalchemy.future import select
from app.models.media import Media
from common_lib.messaging.kafka import send_event


AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET")

s3 = boto3.client("s3", region_name=AWS_REGION)

async def upload_file(file: UploadFile, user_id: str, db):
    key = f"media/{uuid.uuid4()}-{file.filename}"
    s3.upload_fileobj(file.file, S3_BUCKET, key)
    file_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"

    media = Media(id=str(uuid.uuid4()), user_id=user_id, file_url=file_url)
    db.add(media)
    await db.commit()
    await db.refresh(media)

    await send_event("media.uploaded", {
        "media_id": media.id,
        "user_id": media.user_id,
        "file_url": media.file_url
    })

    return {"file_url": file_url, "media_id": media.id}


async def get_media_by_user(user_id: str, db):

    result = await db.execute(select(Media).where(Media.user_id == user_id))
    return result.scalars().all()