import datetime
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime
from bloom.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(request, expiry_time: timedelta):
    payload = request.copy()
    expire_in = datetime.utcnow() + expiry_time
    payload.update({"exp": expire_in})
    return jwt.encode(payload, get_settings().JWT_SECRET, get_settings().JWT_ALGORITHM)


async def create_refresh_token(request):
    return jwt.encode(request, get_settings().JWT_SECRET, get_settings().JWT_ALGORITHM)


def get_token_payload(token):
    try:
        payload = jwt.decode(
            token, get_settings().JWT_SECRET, get_settings().JWT_ALGORITHM
        )
    except JWTError:
        return None
    return payload
