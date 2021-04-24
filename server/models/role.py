"""
User's role API model
"""
from enum import Enum


class Role(Enum):
    """Roles enum"""

    ADMINISTRATOR = "Administrator"
    USER = "User"
