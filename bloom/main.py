from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from .api.router.status import status_router
from .api.router.auth import auth_router
from .api.router.users import user_data_router
from .core.settings.logger import LogConfig
from logging.config import dictConfig
from .models.domain.users_model import Base
from .db.repositories.database_setup import engine
from .services.jwt.jwt_auth_handler import JWTAuth

dictConfig(LogConfig())

Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(status_router.router)
app.include_router(auth_router.router)
app.include_router(user_data_router.router)

app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())
