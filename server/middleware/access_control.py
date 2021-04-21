import time

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED

from server.services.security import TokensHandler

oauth_password_bearer = OAuth2PasswordBearer(tokenUrl="/login")
access_guard = TokensHandler()

async def check_token(token: str = Depends(oauth_password_bearer)):
    try:
        isValid = access_guard.checkToken(token)
        if isValid:
            return True
        else:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    except Exception:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)