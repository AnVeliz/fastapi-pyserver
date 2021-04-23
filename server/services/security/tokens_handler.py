import jwt
from time import time
from datetime import datetime, timedelta

from server.services.configuration.config_reader import ConfigReader
from server.services.configuration.security_config_reader import SecurityConfigReader
from server.services.configuration.all_config_readers import SECURITY_CONFIG_READER

security_config_reader: SecurityConfigReader = ConfigReader().reader(SECURITY_CONFIG_READER)


class TokensHandler:
    def createToken(self, username: str) -> str:
        expiration = datetime.utcnow() + timedelta(minutes=security_config_reader.expiration())
        payload = {"sub": username, "exp": expiration}
        token = jwt.encode(payload, security_config_reader.secret(), algorithm=security_config_reader.algorithm())

        return token

    def checkToken(self, token) -> bool:
        payload = jwt.decode(token, security_config_reader.secret(), algorithms=security_config_reader.algorithm())
        expiration = payload.get("exp")

        return True if time() < expiration else False
