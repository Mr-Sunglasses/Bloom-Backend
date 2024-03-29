from fastapi import APIRouter

from .auth.endpoints import router as auth_router
from .user.endpoints import router as user_router

router = APIRouter(prefix="/api/v1")

router.include_router(auth_router)

router.include_router(user_router)
