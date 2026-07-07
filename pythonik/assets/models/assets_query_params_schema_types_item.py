from enum import Enum


class AssetsQueryParamsSchemaTypesItem(str, Enum):
    ASSET = "ASSET"
    CUSTOM = "CUSTOM"
    LINK = "LINK"
    NLE_PROJECT = "NLE_PROJECT"
    PLACEHOLDER = "PLACEHOLDER"
    POST = "POST"
    SEQUENCE = "SEQUENCE"
    SUBCLIP = "SUBCLIP"

    def __str__(self) -> str:
        return str(self.value)
