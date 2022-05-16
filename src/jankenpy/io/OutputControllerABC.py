from abc import ABC, abstractmethod


class OutputControllerABC(ABC):
    @abstractmethod
    def __call__(self, output: str) -> None:
        """Communicate the output to the player."""
