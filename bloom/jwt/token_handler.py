from fastapi.exceptions import HTTPException
from datetime import timedelta

from ..config import get_settings
from ..models.user import UserModel
from ..security import (
    verify_password_hash,
    create_access_token,
    create_refresh_token,
    get_token_payload,
)
from .schemas import TokenResponseSchema


async def get_token(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.username).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email is not registered with us",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password_hash(data.password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid Login Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    _verify_user_access(user=user)

    return await _get_user_token(user=user)


async def get_refresh_token(token, db):
    payload = get_token_payload(token=token)
    user_id = payload.get("id", None)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Refresh Token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return await _get_user_token(user=user, refresh_token=token)


def _verify_user_access(user: UserModel):
    if not user.is_verified:
        # Trigger user account verification email
        raise HTTPException(
            status_code=400,
            detail="Your account is unverified. We have resent the account verification email.",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def _get_user_token(user: UserModel, refresh_token=None):
    payload = {"id": user.id}

    access_token_expiry = timedelta(
        minutes=get_settings().ACCESS_TOKEN_EXPIRY_MINUTES)

    access_token = await create_access_token(
        request=payload, expiry_time=access_token_expiry
    )

    if not refresh_token:
        refresh_token = await create_refresh_token(request=payload)

    return TokenResponseSchema(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=access_token_expiry.seconds,
    )
