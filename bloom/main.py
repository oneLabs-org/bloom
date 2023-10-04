from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.router.status import status_router
from .api.router.auth import auth_github
from .core.settings.logger import LogConfig
from logging.config import dictConfig

dictConfig(LogConfig())


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
app.include_router(auth_github.router)
