from .hasher import Hasher

TEMPORARY_USERS_LIST = [{"username": "user", "password": "$2b$12$.su540IgA0i1mGxLq9U32uMbk14Q0VBlVXVyuTXTN9wngYUovZOUK"}]

hasher = Hasher()

class AccountChecker:
    def isValidUser(self, username: str, password: str) -> bool:
        user = next(filter(lambda credential: credential["username"] == username, TEMPORARY_USERS_LIST), None)
        return False if user == None else hasher.verifyPassword(password, user["password"])