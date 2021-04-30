"""
Some private API section
"""

from fastapi import APIRouter
from server.models import Account

app_private = APIRouter()


@app_private.post("/account")
async def post_user(account: Account) -> object:
    """Add a new user to the system"""
    return account
