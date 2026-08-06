from enum import Enum


class AnalysisServiceAccountSchemaMethod(str, Enum):
    AMAZON = "AMAZON"
    GOOGLE_AI = "GOOGLE_AI"
    ICONIK = "ICONIK"
    REV_AI = "REV_AI"

    def __str__(self) -> str:
        return str(self.value)
