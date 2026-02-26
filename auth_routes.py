from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth_root():
    """Authentication endpoint"""
    return {"message": "Authentication endpoint"}

