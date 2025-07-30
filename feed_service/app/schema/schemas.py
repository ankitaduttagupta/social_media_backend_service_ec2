from pydantic import BaseModel
from datetime import datetime

class FeedCreateSchema(BaseModel):
    user_id: str
    media_id: str
    file_url: str

class FeedResponseSchema(FeedCreateSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

