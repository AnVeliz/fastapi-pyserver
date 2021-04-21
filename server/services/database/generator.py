from .base import Base, engine
from .account import Account
from .user import User
from .role import Role

def generate_database():
    Base.metadata.create_all(engine)