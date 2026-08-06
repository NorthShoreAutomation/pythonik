from enum import Enum


class StoragePrivateDataSchemaPurpose(str, Enum):
    ARCHIVE = "ARCHIVE"
    EXPORTS = "EXPORTS"
    FACES = "FACES"
    FILES = "FILES"
    KEYFRAMES = "KEYFRAMES"
    PROXIES = "PROXIES"

    def __str__(self) -> str:
        return str(self.value)
