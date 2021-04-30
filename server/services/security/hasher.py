"""
Hashing logic
"""

from passlib.context import CryptContext


class Hasher:
    """It hashes passwords"""

    def __init__(self) -> None:
        self.__password_context = CryptContext(schemes=["bcrypt"])

    def hash_password(self, password: str) -> str:
        """Returns hashed password"""
        return str(self.__password_context.hash(password))

    def verify_password(self, plain_text_password: str, hashed_password: str) -> bool:
        """Verifies password against its hash"""
        try:
            return bool(self.__password_context.verify(plain_text_password, hashed_password))
        except Exception:
            return False
