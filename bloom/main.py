from fastapi import FastAPI
from .api.router.status import status_router
app = FastAPI()

app.include_router(status_router.router)
