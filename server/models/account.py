"""
User's account API model
"""
from pydantic import BaseModel
from .user import User


class Account(BaseModel):
    """Account API model"""

    user: User
    loginName: str
    password: str
    isActive: bool
