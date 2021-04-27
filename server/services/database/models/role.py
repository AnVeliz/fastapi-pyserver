"""
Roles entity
"""
from sqlalchemy import Column, String, Integer
from .base import Base


class Role(Base):
    """Roles entity"""

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column("name", String)
