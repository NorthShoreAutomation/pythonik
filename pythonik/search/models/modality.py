from enum import Enum


class Modality(str, Enum):
    AUDIO = "audio"
    DOCUMENT = "document"
    SPOKEN = "spoken"
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
