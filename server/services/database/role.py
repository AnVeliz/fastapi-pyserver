from sqlalchemy import Column, String, Integer

from .base import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column("name", String)
