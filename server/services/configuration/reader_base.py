"""
Base configuration reader
"""

from abc import ABCMeta, abstractmethod


class ReaderBase(metaclass=ABCMeta):
    """
    Base configuration reader
    """

    @abstractmethod
    def reader_id(self) -> str:
        """Base class with reader_id"""
        raise NotImplementedError()
