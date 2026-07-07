from enum import Enum


class IconikStorageGatewayReadRolesItem(str, Enum):
    CHECKSUM = "CHECKSUM"
    MAIN = "MAIN"
    TRANSCODE = "TRANSCODE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
