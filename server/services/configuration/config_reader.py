"""
Configuration readers repository
"""

from .security_config_reader import SecurityConfigReader
from .database_config_reader import DatabaseConfigReader
from .all_config_readers import ReaderBase, SECURITY_CONFIG_READER, DATABASE_CONFIG_READER


class ConfigReader:
    """Configuration readers repository"""

    def __init__(self):
        self.__config_readers = {
            SECURITY_CONFIG_READER: SecurityConfigReader(),
            DATABASE_CONFIG_READER: DatabaseConfigReader(),
        }

    def reader(self, reader_id: str) -> ReaderBase:
        """Returns the requested reader by Id"""
        return self.__config_readers[reader_id]
