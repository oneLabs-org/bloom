from fastapi import APIRouter, Depends, status, Header, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime
from sqlalchemy.orm import Session
from bloom.jwt.schemas import TokenResponseSchema
from bloom.postgres import get_db
from bloom.auth.schemas import CreateUserRequest
from bloom.security import get_password_hash
from bloom.jwt.token_handler import get_token, get_refresh_token
from bloom.models.user import UserModel

router = APIRouter(
    tags=["auth"], prefix="/auth", responses={404: {"description": "Not Found"}}
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_new_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if user:
        raise HTTPException(
            status_code=422, detail="Email is already registered with us."
        )

    new_user = UserModel(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=get_password_hash(request.password),
        role=request.role,
        registered_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

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
