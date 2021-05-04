"""
A repository of Photos
"""

from os import path, makedirs
from typing import IO
from shutil import copyfileobj
from server.services.configuration import DatabaseConfigReader


class PhotosRepository:
    """Repository of account's photos"""

    def __init__(self, database_config_reader: DatabaseConfigReader):
        self.__database_config_reader = database_config_reader

    def upload(self, user_id: int, photo: IO) -> None:
        """Upload a photo"""
        dir_path = path.abspath(path.join(self.__database_config_reader.files_storage_path(), str(user_id)))
        if not path.exists(dir_path):
            makedirs(dir_path)

        file_path = path.abspath(path.join(*[dir_path, self.__database_config_reader.default_photo_file_name()]))
        with open(file_path, "wb") as buffer:
            copyfileobj(photo, buffer)
