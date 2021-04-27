"""
Database
"""

from .models.base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.services.configuration import ConfigReader, DatabaseConfigReader, DATABASE_CONFIG_READER


database_config_reader: DatabaseConfigReader = ConfigReader().reader(DATABASE_CONFIG_READER)
engine = create_engine(database_config_reader.connection())

Session = sessionmaker(bind=engine)


def generate_database_schema():
    """Generates database schema"""
    Base.metadata.create_all(engine)
