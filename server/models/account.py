"""
User's account API model
"""
from pydantic import BaseModel  # pylint: disable=E0611
from .user import User


# pylint: disable=R0903
class Account(BaseModel):
    """Account API model"""

    user: User
    loginName: str
    password: str
    isActive: bool
