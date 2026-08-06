from enum import Enum


class AssetPostElasticSchemaType(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
