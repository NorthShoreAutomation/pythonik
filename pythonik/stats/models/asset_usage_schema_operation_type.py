from enum import Enum


class AssetUsageSchemaOperationType(str, Enum):
    APPROVE = "APPROVE"
    COMMENT = "COMMENT"
    CREATE = "CREATE"
    DELETE = "DELETE"
    EXIT = "EXIT"
    PAUSE = "PAUSE"
    PLAY = "PLAY"
    REFOCUS = "REFOCUS"
    REJECT = "REJECT"
    RENAME = "RENAME"
    SEEK = "SEEK"
    UNFOCUS = "UNFOCUS"
    VIEW = "VIEW"

    def __str__(self) -> str:
        return str(self.value)
