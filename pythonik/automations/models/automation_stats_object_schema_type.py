from enum import Enum


class AutomationStatsObjectSchemaType(str, Enum):
    GAUGE = "GAUGE"

    def __str__(self) -> str:
        return str(self.value)
