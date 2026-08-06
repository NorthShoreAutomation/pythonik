from enum import Enum


class PublishFeatureParametersRegion(str, Enum):
    EU = "EU"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
