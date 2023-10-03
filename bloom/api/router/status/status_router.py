from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

from ....core.settings.config import Config, get_settings
import logging

logger = logging.getLogger("Bloom")

router = APIRouter(
    prefix="/bloom/v1/status",
    tags=["status"]
)


@router.get("", status_code=status.HTTP_200_OK)
def check_api_status(settings: Annotated[Config, Depends(get_settings)]):
    logger.info(f"{settings.TEST}")
    return {"status": "working"}
