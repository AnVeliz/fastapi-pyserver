"""
Account entity
"""

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base


class Account(Base):
    """Account entity"""

    __tablename__ = "accounts"
    __table_args__ = (UniqueConstraint("user_id"),)

    id = Column(Integer, primary_key=True)
    login = Column("login", String)
    password = Column("password", String)
    isActive = Column("is_active", Boolean)

    userId = Column("user_id", Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="account")
