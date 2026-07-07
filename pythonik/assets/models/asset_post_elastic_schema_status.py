from enum import Enum


class AssetPostElasticSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
