from pydantic import BaseModel
from fastapi import Query
from .role import Role

class User(BaseModel):
    id: int
    firstName: str
    middleName: str
    lastName: str
    email: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    role: Role