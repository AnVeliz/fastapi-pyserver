"""
Database initialization logic
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from server.services.configuration import ConfigReader, DatabaseConfigReader, DATABASE_CONFIG_READER

database_config_reader: DatabaseConfigReader = ConfigReader().reader(DATABASE_CONFIG_READER)
engine = create_engine(database_config_reader.connection())

Session = sessionmaker(bind=engine)
Base = declarative_base()
