from enum import Enum


class BulkShareCreateSchemaDrm(str, Enum):
    NONE = "none"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
