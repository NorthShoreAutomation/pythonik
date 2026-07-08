from enum import Enum


class UserEditInternalSchemaOnboardingGoal(str, Enum):
    CENTRALIZE = "CENTRALIZE"
    COLLABORATE = "COLLABORATE"
    REVISIT = "REVISIT"

    def __str__(self) -> str:
        return str(self.value)
