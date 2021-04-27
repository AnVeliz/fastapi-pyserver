"""
Base configuration reader
"""

CONFIG_UNDEFINED = "CONFIG_UNDEFINED"


class ReaderBase:
    """
    Base configuration reader
    """

    def reader_id(self) -> str:
        """Unique identifier of a reader"""
        return CONFIG_UNDEFINED
