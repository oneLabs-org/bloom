from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/bloom/v1/auth",
    tags=["auth"]
)
