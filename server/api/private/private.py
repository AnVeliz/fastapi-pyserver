"""
Some private API section
"""

from fastapi import APIRouter, File, UploadFile
from server.models import Account
from server.models import User
from server.services.database import get_photos_repository

app_private = APIRouter()


@app_private.post("/account")
async def post_account(account: Account) -> object:
    """Add a new account"""
    return account


@app_private.post("/{user_id}/user-info")
async def post_user_info(user_id: int, user: User) -> object:
    """Add a new user"""
    return user


@app_private.post("/{user_id}/photo")
async def post_user_photo(user_id: int, photo: UploadFile = File(...)) -> object:
    """Add a photo to an account"""
    # await post(UPLOAD_PHOTO_URL, files={"image": file})
    get_photos_repository().upload(user_id, photo.file)
    return None
