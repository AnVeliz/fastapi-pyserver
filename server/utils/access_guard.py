import jwt
from time import time
from datetime import datetime, timedelta

from server.config.config_reader import ConfigReader
from server.config.security_config_reader import SecurityConfigReader
from server.config.all_config_readers import SECURITY_CONFIG_READER

security_config_reader: SecurityConfigReader = ConfigReader().reader(SECURITY_CONFIG_READER)

class AccessGuard:
    def createToken(self, credentials) -> str:
        expiration = datetime.utcnow() + timedelta(minutes=security_config_reader.expiration())
        payload = {
            "sub": credentials["username"],
            "role": credentials["password"],
            "exp": expiration
        }
        token = jwt.encode(payload, security_config_reader.secret(), algorithm=security_config_reader.algorithm())

        return token

    def checkToken(self, token) -> bool:
        payload = jwt.decode(token, security_config_reader.secret(), algorithms=security_config_reader.algorithm())
        expiration = payload.get("exp")

        return True if time() < expiration else False