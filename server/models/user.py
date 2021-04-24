"""
User API model
"""
from pydantic import BaseModel  # pylint: disable=E0611
from fastapi import Query
from .role import Role


# pylint: disable=R0903
class User(BaseModel):
    """User API model"""

    id: int
    firstName: str
    middleName: str
    lastName: str
    email: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")  # noqa: W605 # pylint: disable=W1401
    role: Role
