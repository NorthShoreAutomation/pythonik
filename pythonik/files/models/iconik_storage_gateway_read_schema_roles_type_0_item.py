from enum import Enum


class IconikStorageGatewayReadSchemaRolesType0Item(str, Enum):
    CHECKSUM = "CHECKSUM"
    MAIN = "MAIN"
    TRANSCODE = "TRANSCODE"
    TRANSFER = "TRANSFER"

    def __str__(self) -> str:
        return str(self.value)
