from enum import Enum


class IconikStorageGatewayTelemetrySchemaStartStatus(str, Enum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
