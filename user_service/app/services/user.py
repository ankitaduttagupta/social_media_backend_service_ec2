from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.db.database import get_db
from common_lib.messaging.kafka import send_event
import uuid

async def signup_user(data: dict, db: AsyncSession = None):
    user_id = str(uuid.uuid4())
    user = User(id=user_id, email=data["email"])
    db.add(user)
    await db.commit()
    await db.refresh(user)
    await send_event("user.created",
                     {"user_id": user_id, "email": user.email})
    return {"message": "User created",
            "user": {"id": user.id, "email": user.email}}