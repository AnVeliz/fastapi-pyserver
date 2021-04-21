from passlib.context import CryptContext

class Hasher:
    def __init__(self):
        self.__passwordContext = CryptContext(schemes=["bcrypt"])

    def hashPassword(self, password: str) -> str:
        return self.__passwordContext.hash(password)

    def verifyPassword(self, plainTextPassword: str, hashedPassword: str) -> bool:
        try:
            return self.__passwordContext.verify(plainTextPassword, hashedPassword)
        except Exception as e:
            return False