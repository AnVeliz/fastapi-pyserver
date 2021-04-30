"""
Some public API section
"""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED
from server.services.security import TokensHandler, AccountChecker

app_public = APIRouter()
account_checker = AccountChecker()
tokens_handler = TokensHandler()


@app_public.get("/health")
async def health_check() -> object:
    """health check"""
    return {"Status": "OK"}


@app_public.post("/login")
async def login(password_request_form: OAuth2PasswordRequestForm = Depends()) -> object:
    """Login entrypoint"""
    if not account_checker.is_valid_user(password_request_form.username, password_request_form.password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    token = tokens_handler.create_token(password_request_form.username)
    return {"access_token": token}
