from enum import Enum


class FileElasticSchemaType(str, Enum):
    DIRECTORY = "DIRECTORY"
    FILE = "FILE"
    SEQUENCE = "SEQUENCE"
    SYMLINK = "SYMLINK"

    def __str__(self) -> str:
        return str(self.value)
