from os.path import dirname, join
from yaml import load, FullLoader
from .all_config_readers import ReaderBase, SECURITY_CONFIG_FILENAME, SECURITY_CONFIG_READER


class SecurityConfigReader(ReaderBase):
    def __init__(self):
        with open(join(dirname(__file__), SECURITY_CONFIG_FILENAME), "r") as securityConfigFile:
            configData = load(securityConfigFile, Loader=FullLoader)
            jwtConfig = configData[0]["jwt"]
            self.__jwtSecret = jwtConfig["secret"]
            self.__jwtAlgorithm = jwtConfig["algorithm"]
            self.__jwtExpiration = jwtConfig["expire"]

    def readerId(self) -> str:
        return SECURITY_CONFIG_READER

    def secret(self) -> str:
        return self.__jwtSecret

    def algorithm(self) -> str:
        return self.__jwtAlgorithm

    def expiration(self) -> int:
        return self.__jwtExpiration
