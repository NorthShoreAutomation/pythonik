from enum import Enum


class TriggerCustomActionParametersContext(str, Enum):
    ASSET = "ASSET"
    ASSET_SUBCLIP = "ASSET_SUBCLIP"
    BULK = "BULK"

    def __str__(self) -> str:
        return str(self.value)
