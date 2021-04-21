from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED
from server.services.security import TokensHandler, AccountChecker

app_public = APIRouter()
account_checker = AccountChecker()
tokens_handler = TokensHandler()

@app_public.get("/health")
async def health_check():
    return { "Status": "I'm alive." }

@app_public.post("/login")
async def login(passwordRequestForm: OAuth2PasswordRequestForm = Depends()):
    if not account_checker.isValidUser(passwordRequestForm.username, passwordRequestForm.password):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    token = tokens_handler.createToken(passwordRequestForm.username)
    return {"access_token": token}
