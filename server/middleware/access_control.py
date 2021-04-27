"""
Access guard hook
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from server.services.security import TokensHandler

oauth_password_bearer = OAuth2PasswordBearer(tokenUrl="/login")
access_guard = TokensHandler()


async def check_token(token: str = Depends(oauth_password_bearer)):
    """Check if user is active"""
    try:
        is_valid = access_guard.check_token(token)
        if is_valid:
            return True
        else:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    except Exception:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
