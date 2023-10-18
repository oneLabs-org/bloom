from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from .jwt.auth_handler import JWTAuth
from .api import router
from logging import Logger

logger = Logger(name="Bloom Logger")
origins = ["*"]


def configure_cors(app: FastAPI) -> None:

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(title="Bloom API")
    configure_cors(app=app)

    app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

    app.include_router(router=router)

    return app


logger.info("Starting Bloom API")
app = create_app()
