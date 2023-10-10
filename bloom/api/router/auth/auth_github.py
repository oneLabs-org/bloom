from .auth_router import router
from typing import Annotated, Dict
from starlette.responses import RedirectResponse
from fastapi import Depends, status
from ....core.settings.config import Config, get_settings
import httpx


@router.get("/github-login")
async def github_auth(settings: Annotated[Config, Depends(get_settings)]):
    return RedirectResponse(
        f"https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}",
        status_code=status.HTTP_302_FOUND,
    )


@router.get("/github-code")
async def github_code(code: str, settings: Annotated[Config, Depends(get_settings)]):
    params: Dict[str, str] = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
    }

    headers: Dict[str, str] = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://github.com/login/oauth/access_token",
            params=params,
            headers=headers,
        )

    response_json = response.json()
    access_token = response_json["access_token"]

    async with httpx.AsyncClient() as client:
        headers.update({"Authorization": f"Bearer {access_token}"})
        response = await client.get("https://api.github.com/user", headers=headers)

    return response.json()
