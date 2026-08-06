from enum import Enum


class IconikStorageGatewayTelemetrySchemaStatus(str, Enum):
    ERROR = "ERROR"
    LIVE = "LIVE"
    OFFLINE = "OFFLINE"
    STOPPED = "STOPPED"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
