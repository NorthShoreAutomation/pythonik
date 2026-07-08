from enum import Enum


class TriggerSchemaRealm(str, Enum):
    ENTITY = "ENTITY"
    FILES = "FILES"
    FORMATS = "FORMATS"
    JOBS = "JOBS"
    METADATA = "METADATA"
    SHARES = "SHARES"

    def __str__(self) -> str:
        return str(self.value)
