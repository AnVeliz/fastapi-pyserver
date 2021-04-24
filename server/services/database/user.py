from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstName = Column("first_name", String)
    middleName = Column("middle_name", String)
    lastName = Column("last_name", String)
    email = Column("email", String)

    roleId = Column("role_id", Integer, ForeignKey("roles.id"))
    role = relationship("Role")

    account = relationship("Account", uselist=False, back_populates="users")
