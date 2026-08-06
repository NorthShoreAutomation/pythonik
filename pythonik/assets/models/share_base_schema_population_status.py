from enum import Enum


class ShareBaseSchemaPopulationStatus(str, Enum):
    FINISHED = "FINISHED"
    POPULATING = "POPULATING"

    def __str__(self) -> str:
        return str(self.value)
