from pydantic import BaseModel
from .user import User

class Account(BaseModel):
    user: User
    loginName: str
    password: str
    isActive: bool