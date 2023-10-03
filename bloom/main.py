from fastapi import FastAPI
from .api.router.status import status_router
from .api.router.auth import auth_github
from .core.settings.logger import LogConfig
from logging.config import dictConfig

dictConfig(LogConfig())


app = FastAPI()


app.include_router(status_router.router)
app.include_router(auth_github.router)
