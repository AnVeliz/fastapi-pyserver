"""
Security configuration reader
"""

from os.path import dirname, join
from yaml import load, FullLoader
from .all_config_readers import ReaderBase

SECURITY_CONFIG_FILENAME = "security.yaml"
SECURITY_CONFIG_UNDEFINED = "SECURITY_CONFIG_UNDEFINED"
SECURITY_CONFIG_READER = "SECURITY_CONFIG_READER"


class SecurityConfigReader(ReaderBase):
    """Security configuration reader"""

    __jwt_secret = "1cadc5f5413a21d521f532c57e1e5ea31c4fe325df2x4fd54d8f5e3154562a5"
    __jwt_algorithm = "HS256"
    __jwt_expiration = "1"

    def __init__(self):
        try:
            with open(join(dirname(__file__), SECURITY_CONFIG_FILENAME), "r") as security_config_file:
                config_data = load(security_config_file, Loader=FullLoader)
                jwt_config = config_data[0]["jwt"]
                self.__jwt_secret = jwt_config["secret"]
                self.__jwt_algorithm = jwt_config["algorithm"]
                self.__jwt_expiration = jwt_config["expire"]
        except FileNotFoundError:
            print("Security configuration file is not found.")

    def reader_id(self) -> str:
        """Security config Id"""
        return SECURITY_CONFIG_READER

    def secret(self) -> str:
        """Returns jwt secret"""
        return self.__jwt_secret

    def algorithm(self) -> str:
        """Returns jwt algorithm"""
        return self.__jwt_algorithm

    def expiration(self) -> float:
        """Returns jwt token expiration time"""
        return float(self.__jwt_expiration)
