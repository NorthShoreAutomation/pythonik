from enum import Enum


class IconikStorageGatewayReadRolesType0Item(str, Enum):
    CHECKSUM = "CHECKSUM"
    MAIN = "MAIN"
    TRANSCODE = "TRANSCODE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
