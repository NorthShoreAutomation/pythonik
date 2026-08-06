from enum import Enum


class FileSetElasticSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
