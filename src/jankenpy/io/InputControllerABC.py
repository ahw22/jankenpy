from abc import ABC, abstractmethod


class InputControllerABC(ABC):
    @abstractmethod
    def get_player_name(self) -> str:
        """Method that asks a players name."""

    @abstractmethod
    def get_player_choice(self) -> int:
        """Get the choice of move the player wants to make."""
