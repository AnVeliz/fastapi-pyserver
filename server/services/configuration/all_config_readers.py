SECURITY_CONFIG_FILENAME = "security.yaml"
SECURITY_CONFIG_UNDEFINED = "SECURITY_CONFIG_UNDEFINED"
SECURITY_CONFIG_READER = "SECURITY_CONFIG_READER"

DATABASE_CONFIG_FILENAME = "database.yaml"
DATABASE_CONFIG_UNDEFINED = "DATABASE_CONFIG_UNDEFINED"
DATABASE_CONFIG_READER = "DATABASE_CONFIG_READER"

class ReaderBase:
    def readerId(self) -> str:
        return SECURITY_CONFIG_UNDEFINED