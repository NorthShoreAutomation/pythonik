from enum import Enum


class CollectionExportSchemaMetadataFormat(str, Enum):
    CSV = "CSV"
    JSON = "JSON"
    XML = "XML"

    def __str__(self) -> str:
        return str(self.value)
