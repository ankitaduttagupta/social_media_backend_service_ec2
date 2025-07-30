from sqlalchemy import Column, String, Integer, Text, DateTime
from app.db.database import Base
from datetime import datetime

class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    media_id = Column(String, nullable=False)
    file_url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)

