from fastapi import APIRouter, HTTPException, status

router = APIRouter(
    prefix="/bloom/v1/status",
    tags=["status"]
)


@router.get("/", status_code=status.HTTP_200_OK)
def check_api_status():
    return {"status": "working"}
