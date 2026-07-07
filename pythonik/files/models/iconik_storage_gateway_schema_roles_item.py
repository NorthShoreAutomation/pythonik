from enum import Enum


class IconikStorageGatewaySchemaRolesItem(str, Enum):
    CHECKSUM = "CHECKSUM"
    MAIN = "MAIN"
    TRANSCODE = "TRANSCODE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
