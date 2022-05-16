from abc import ABC, abstractmethod
from typing import Callable, Optional


class InputControllerABC(ABC):
    @abstractmethod
    def get_str(self, validator: Optional[Callable] = None) -> str:
        """Method that gets a string."""

    @abstractmethod
    def get_int(self, validator: Optional[Callable] = None) -> int:
        """Method that gets an int."""
