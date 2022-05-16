from dataclasses import dataclass

from jankenpy.io.InputControllerABC import InputControllerABC
from jankenpy.io.OutputControllerABC import OutputControllerABC


@dataclass
class IOController:
    inputcontroller: InputControllerABC
    outputcontroller: OutputControllerABC
