from os.path import dirname, join
from yaml import load, FullLoader
from .all_config_readers import ReaderBase, SECURITY_CONFIG_FILENAME, SECURITY_CONFIG_READER


class SecurityConfigReader(ReaderBase):
    __jwtSecret = "1cadc5f5413a21d521f532c57e1e5ea31c4fe325df2x4fd54d8f5e3154562a5"
    __jwtAlgorithm = "HS256"
    __jwtExpiration = "1"

    def __init__(self):
        try:
            with open(join(dirname(__file__), SECURITY_CONFIG_FILENAME), "r") as securityConfigFile:
                configData = load(securityConfigFile, Loader=FullLoader)
                jwtConfig = configData[0]["jwt"]
                self.__jwtSecret = jwtConfig["secret"]
                self.__jwtAlgorithm = jwtConfig["algorithm"]
                self.__jwtExpiration = jwtConfig["expire"]
        except FileNotFoundError:
            print("Security configuration file is not found.")

    def readerId(self) -> str:
        return SECURITY_CONFIG_READER

    def secret(self) -> str:
        return self.__jwtSecret

    def algorithm(self) -> str:
        return self.__jwtAlgorithm

    def expiration(self) -> int:
        return self.__jwtExpiration
