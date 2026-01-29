from enum import Enum


class EnumSingleton(Enum):
    INSTANCE = object()

    def any_method(self) -> None:
        # any logic here
        ...

# Usage: EnumSingleton.INSTANCE.any_method()
