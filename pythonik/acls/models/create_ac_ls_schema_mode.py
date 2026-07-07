from enum import Enum


class CreateACLsSchemaMode(str, Enum):
    APPEND = "APPEND"
    OVERWRITE = "OVERWRITE"

    def __str__(self) -> str:
        return str(self.value)
