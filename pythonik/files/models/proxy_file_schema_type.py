from enum import Enum


class ProxyFileSchemaType(str, Enum):
    DIRECTORY = "DIRECTORY"
    FILE = "FILE"
    SEQUENCE = "SEQUENCE"
    SYMLINK = "SYMLINK"

    def __str__(self) -> str:
        return str(self.value)
