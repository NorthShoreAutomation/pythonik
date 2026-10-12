from enum import Enum


class Tier(str, Enum):
    PREFER = "prefer"
    REQUIRE = "require"
    TRY = "try"

    def __str__(self) -> str:
        return str(self.value)
