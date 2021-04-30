"""
A repository of Users and their Accounts
"""

from sqlalchemy.orm import Session
from server.services.database.models import Account


class AccountsRepository:
    """A repository for users' accounts"""

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get(self, login: str) -> Account:
        """Get an account"""
        account = Account(self.__session().query(Account).filter_by(login=login).one())
        return account
