from starlette.authentication import AuthCredentials, UnauthenticatedUser
from fastapi import Depends
from ..security.hash_password import oauth2_scheme
from ...models.domain.users_model import UserModel
from ...db.repositories.database_setup import get_db
from ..security.hash_password import get_token_payload


def get_current_user(token: str = Depends(oauth2_scheme), db=None):
    payload = get_token_payload(token)
    if not payload or type(payload) is not dict:
        return None

    user_id = payload.get("id", None)
    if not user_id:
        return None

    if not db:
        db = next(get_db())

    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user


class JWTAuth:
    async def authenticate(self, conn):
        guest = AuthCredentials(["unauthenticated"]), UnauthenticatedUser()

        if "Authorization" not in conn.headers:
            return guest

        token = conn.headers.get("Authorization").split(" ")[1]  # Bearer token_hash
        if not token:
            return guest

        user = get_current_user(token=token)

        if not user:
            return guest

        return AuthCredentials("Authenticated"), user
