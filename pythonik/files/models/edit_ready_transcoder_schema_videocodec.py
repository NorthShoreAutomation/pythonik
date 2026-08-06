from enum import Enum


class EditReadyTranscoderSchemaVideocodec(str, Enum):
    APPLE_PRORES_422 = "Apple_ProRes_422"
    APPLE_PRORES_422_HQ = "Apple_ProRes_422_HQ"
    APPLE_PRORES_422_LT = "Apple_ProRes_422_LT"
    APPLE_PRORES_422_PROXY = "Apple_ProRes_422_Proxy"
    APPLE_PRORES_4444 = "Apple_ProRes_4444"

    def __str__(self) -> str:
        return str(self.value)
