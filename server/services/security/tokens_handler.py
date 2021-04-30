"""
It works with tokens
"""

from time import time
from datetime import datetime, timedelta
from jwt import decode, encode
from server.services.configuration.config_reader import ConfigReader
from server.services.configuration.security_config_reader import SecurityConfigReader, SECURITY_CONFIG_READER

security_config_reader: SecurityConfigReader = ConfigReader().reader(SECURITY_CONFIG_READER)  # type: ignore


class TokensHandler:
    """It processes tokens"""

    def create_token(self, username: str) -> str:
        """Create a new token"""
        expiration = datetime.utcnow() + timedelta(minutes=security_config_reader.expiration())
        payload = {"sub": username, "exp": expiration}
        token = encode(payload, security_config_reader.secret(), algorithm=security_config_reader.algorithm())

        return token

    def check_token(self, token: str) -> bool:
        """It checks if a token is valid"""
        payload = decode(token, security_config_reader.secret(), algorithms=[security_config_reader.algorithm()])
        expiration_payload = payload.get("exp")
        expiration = expiration_payload if expiration_payload is not None else 0  # type: float

        return True if time() < expiration else False
