"""
Database config reader
"""

from os.path import dirname, join
from yaml import load, FullLoader
from .reader_base import ReaderBase

DATABASE_CONFIG_FILENAME = "database.yaml"
DATABASE_CONFIG_UNDEFINED = "DATABASE_CONFIG_UNDEFINED"
DATABASE_CONFIG_READER = "DATABASE_CONFIG_READER"


class DatabaseConfigReader(ReaderBase):
    """Database config reader"""

    __connection = "postgresql+psycopg2://postgres:root@localhost:5432/pyserver"
    __files_storage_path = "./tmp/files/"
    __default_photo_file_name = "photo.png"

    def __init__(self) -> None:
        try:
            with open(join(dirname(__file__), DATABASE_CONFIG_FILENAME), "r") as database_config_file:
                config_data = load(database_config_file, Loader=FullLoader)
                database_config = config_data[0]["database"]
                self.__connection = database_config["connection"]
                self.__files_storage_path = database_config["filesStoragePath"]
                self.__default_photo_file_name = database_config["defaultPhotoFileName"]
        except FileNotFoundError:
            print("Database configuration file is not found.")

    def reader_id(self) -> str:
        """Returns database reader id"""
        return DATABASE_CONFIG_READER

    def connection(self) -> str:
        """Returns connection string"""
        return self.__connection

    def files_storage_path(self) -> str:
        """Returns files storage path string"""
        return self.__files_storage_path

    def default_photo_file_name(self) -> str:
        """Returns default photo file name string"""
        return self.__default_photo_file_name
