from dataclasses import dataclass

from InputControllerABC import InputControllerABC
from OutputControllerABC import OutputControllerABC


@dataclass
class IOController:
    inputcontroller: InputControllerABC
    outputcontroller: OutputControllerABC
