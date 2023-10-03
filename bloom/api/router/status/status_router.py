from fastapi import APIRouter, status
from typing import Annotated
import logging

logger = logging.getLogger("Bloom")

router = APIRouter(
    prefix="/bloom/v1/status",
    tags=["status"]
)


@router.get("", status_code=status.HTTP_200_OK)
def check_api_status():
    return {"status": "working"}
