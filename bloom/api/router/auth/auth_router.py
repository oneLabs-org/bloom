from fastapi import APIRouter, Depends, status, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ....models.schemas.token_response_schema import TokenResponseSchema
from ....db.repositories.database_setup import get_db
from ....models.schemas.user_model_schema import CreateUserRequest
from ....db.queries.user_model_queries import create_user_account
from ....services.jwt.jwt_token_handler import get_token, get_refresh_token

router = APIRouter(
    prefix="/bloom/v1/auth/user",
    tags=["auth"],
    responses={404: {"description": "Not Found"}},
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_new_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=request, db=db)
    return {"Message": "User Account has been Successfully Created"}


@router.post("/token", status_code=status.HTTP_200_OK)
async def authenticate_user(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    return await get_token(data=request, db=db)


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh_access_token(
    refresh_token: str = Header(), db: Session = Depends(get_db)
):
    return await get_refresh_token(token=refresh_token, db=db)
