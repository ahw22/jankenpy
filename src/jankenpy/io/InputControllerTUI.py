from typing import Any, Callable, Optional

from jankenpy.io.InputControllerABC import InputControllerABC


class TUIInputController(InputControllerABC):
    @staticmethod
    def _get_value_via_TUI_input(validator: Optional[Callable], expected_type: type) -> Any:
        value = expected_type(input(""))
        if validator is not None and not validator(value):
            raise ValueError(f"Incorrect input: {value}")

        return value

    def get_str(self, validator=None) -> str:
        return self._get_value_via_TUI_input(validator, str)

    def get_int(self, validator=None) -> int:
        return self._get_value_via_TUI_input(validator, int)
