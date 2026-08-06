from enum import Enum


class GetShareSchemaPopulationStatus(str, Enum):
    FINISHED = "FINISHED"
    POPULATING = "POPULATING"

    def __str__(self) -> str:
        return str(self.value)
