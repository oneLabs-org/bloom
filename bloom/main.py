from fastapi import FastAPI
from .api.router.status import status_router
from .core.settings.logger import LogConfig
from logging.config import dictConfig

dictConfig(LogConfig())


app = FastAPI()


app.include_router(status_router.router)
