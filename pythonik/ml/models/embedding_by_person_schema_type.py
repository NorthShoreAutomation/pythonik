from enum import Enum


class EmbeddingByPersonSchemaType(str, Enum):
    AUGMENTED = "AUGMENTED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
