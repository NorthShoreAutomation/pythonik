from enum import Enum


class MetadataFieldValueUpdateSchemaMode(str, Enum):
    APPEND = "append"
    DELETE = "delete"
    OVERWRITE = "overwrite"

    def __str__(self) -> str:
        return str(self.value)
