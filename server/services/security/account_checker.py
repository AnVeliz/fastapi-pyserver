"""
Service of account validation
"""

from server.services.database import get_accounts_repository
from .hasher import Hasher

# TEMPORARY_USERS_LIST = [{"username": "user", "password": "$2b$12$.su540IgA0i1mGxLq9U32uMbk14Q0VBlVXVyuTXTN9wngYUovZOUK"}]

hasher = Hasher()


class AccountChecker:
    """It checks users' accounts"""

    def is_valid_user(self, username: str, password: str) -> bool:
        """Checks if users are valid"""
        # user = next(filter(lambda credential: credential["username"] == username, TEMPORARY_USERS_LIST), None)
        account = get_accounts_repository().get(username)
        return False if account is None else hasher.verify_password(password, account.password)
