from enum import Enum


class ExportActionParametersMetadataFormat(str, Enum):
    CSV = "CSV"
    JSON = "JSON"
    XML = "XML"

    def __str__(self) -> str:
        return str(self.value)
