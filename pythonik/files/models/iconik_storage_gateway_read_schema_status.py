from enum import Enum


class IconikStorageGatewayReadSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    OFFLINE = "OFFLINE"
    STOPPED = "STOPPED"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
