from os.path import dirname, join
from yaml import load, FullLoader
from .all_config_readers import ReaderBase, DATABASE_CONFIG_FILENAME, DATABASE_CONFIG_READER


class DatabaseConfigReader(ReaderBase):
    __connection = "postgresql+psycopg2://postgres:root@localhost:5432/pyserver"

    def __init__(self):
        try:
            with open(join(dirname(__file__), DATABASE_CONFIG_FILENAME), "r") as databaseConfigFile:
                configData = load(databaseConfigFile, Loader=FullLoader)
                databaseConfig = configData[0]["database"]
                self.__connection = databaseConfig["connection"]
        except FileNotFoundError:
            print("Database configuration file is not found.")

    def readerId(self) -> str:
        return DATABASE_CONFIG_READER

    def connection(self) -> str:
        return self.__connection
