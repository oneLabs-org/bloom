from fastapi import APIRouter

from bloom.auth.endpoints import router as auth_router
from bloom.user.endpoints import router as user_router
from bloom.health.endpoints import router as health_router

router = APIRouter(prefix="/api/v1")

router.include_router(health_router)

router.include_router(auth_router)

router.include_router(user_router)
