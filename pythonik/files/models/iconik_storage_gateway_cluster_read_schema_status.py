from enum import Enum


class IconikStorageGatewayClusterReadSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    OFFLINE = "OFFLINE"
    STOPPED = "STOPPED"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
