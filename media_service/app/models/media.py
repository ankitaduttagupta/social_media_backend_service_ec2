from sqlalchemy import Column, String
from app.db.database import Base

class Media(Base):
    __tablename__ = "media"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    file_url = Column(String)