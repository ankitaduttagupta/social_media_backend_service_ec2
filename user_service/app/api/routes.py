
from fastapi import APIRouter
from app.services.user import signup_user

router = APIRouter()

@router.post("/signup")
async def signup(data: dict):
    return await signup_user(data)
