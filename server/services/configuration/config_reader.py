from .security_config_reader import SecurityConfigReader
from .database_config_reader import DatabaseConfigReader
from .all_config_readers import ReaderBase, SECURITY_CONFIG_READER, DATABASE_CONFIG_READER


class ConfigReader:
    def __init__(self):
        self.__configReaders = {
            SECURITY_CONFIG_READER: SecurityConfigReader(),
            DATABASE_CONFIG_READER: DatabaseConfigReader(),
        }

    def reader(self, readerId: str) -> ReaderBase:
        return self.__configReaders[readerId]
