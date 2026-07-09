from enum import Enum


class FileSetElasticSchemaType(str, Enum):
    MANY_FILES = "MANY_FILES"
    REGULAR = "REGULAR"

    def __str__(self) -> str:
        return str(self.value)
