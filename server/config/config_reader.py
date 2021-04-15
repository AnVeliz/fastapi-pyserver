from .security_config_reader import SecurityConfigReader
from .all_config_readers import ReaderBase, SECURITY_CONFIG_READER

class ConfigReader:
    def __init__(self):
        self.__configReaders = {
            SECURITY_CONFIG_READER: SecurityConfigReader()
        }

    def reader(self, readerId: str) -> ReaderBase:
        return self.__configReaders[readerId]