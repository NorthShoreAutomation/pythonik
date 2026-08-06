from enum import Enum


class EmbeddingSchemaType(str, Enum):
    AUGMENTED = "AUGMENTED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
