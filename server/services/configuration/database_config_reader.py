"""
Database config reader
"""

from os.path import dirname, join
from yaml import load, FullLoader
from .all_config_readers import ReaderBase

DATABASE_CONFIG_FILENAME = "database.yaml"
DATABASE_CONFIG_UNDEFINED = "DATABASE_CONFIG_UNDEFINED"
DATABASE_CONFIG_READER = "DATABASE_CONFIG_READER"


class DatabaseConfigReader(ReaderBase):
    """Database config reader"""

    __connection = "postgresql+psycopg2://postgres:root@localhost:5432/pyserver"

    def __init__(self) -> None:
        try:
            with open(join(dirname(__file__), DATABASE_CONFIG_FILENAME), "r") as database_config_file:
                config_data = load(database_config_file, Loader=FullLoader)
                database_config = config_data[0]["database"]
                self.__connection = database_config["connection"]
        except FileNotFoundError:
            print("Database configuration file is not found.")

    def reader_id(self) -> str:
        """Returns database reader id"""
        return DATABASE_CONFIG_READER

    def connection(self) -> str:
        """Returns connection string"""
        return self.__connection
