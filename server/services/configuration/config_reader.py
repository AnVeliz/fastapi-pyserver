"""
Configuration readers repository
"""

from .security_config_reader import SecurityConfigReader, SECURITY_CONFIG_READER
from .database_config_reader import DatabaseConfigReader, DATABASE_CONFIG_READER
from .reader_base import ReaderBase


class ConfigReader:
    """Configuration readers repository"""

    def __init__(self) -> None:
        self.__config_readers = {
            SECURITY_CONFIG_READER: SecurityConfigReader(),
            DATABASE_CONFIG_READER: DatabaseConfigReader(),
        }

    def reader(self, reader_id: str) -> ReaderBase:
        """Returns the requested reader by Id"""
        return self.__config_readers[reader_id]
