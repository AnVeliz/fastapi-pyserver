"""
Database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.services.configuration import ConfigReader, DatabaseConfigReader, DATABASE_CONFIG_READER
from .repository import AccountsRepository

database_config_reader: DatabaseConfigReader = ConfigReader().reader(DATABASE_CONFIG_READER)  # type: ignore
engine = create_engine(database_config_reader.connection())
Session = sessionmaker(bind=engine)

accounts_repository: AccountsRepository = AccountsRepository(Session)


def get_accounts_repository() -> AccountsRepository:
    """Always returns users account repository for now only"""
    return accounts_repository
