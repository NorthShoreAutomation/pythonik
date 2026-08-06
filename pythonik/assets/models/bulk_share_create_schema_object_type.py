from enum import Enum


class BulkShareCreateSchemaObjectType(str, Enum):
    ASSETS = "assets"

    def __str__(self) -> str:
        return str(self.value)
