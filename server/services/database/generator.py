"""
Database generator
"""
from .base import Base, engine


def generate_database():
    """Generates database"""
    Base.metadata.create_all(engine)
