"""
A repository of Users and their Accounts
"""

from typing import cast, Optional
from sqlalchemy.orm import Session
from server.services.database.models import Account


class AccountsRepository:
    """A repository for users' accounts"""

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get(self, login: str) -> Optional[Account]:
        """Get an account"""
        db_account = self.__session().query(Account).filter_by(login=login).one_or_none()
        return cast(Account, db_account) if db_account is not None else None
