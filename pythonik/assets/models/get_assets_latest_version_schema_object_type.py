from enum import Enum


class GetAssetsLatestVersionSchemaObjectType(str, Enum):
    ASSETS = "assets"

    def __str__(self) -> str:
        return str(self.value)
