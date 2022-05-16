from typing import Callable

from jankenpy.io.OutputControllerABC import OutputControllerABC


class TUIPrinter(OutputControllerABC):
    def __init__(self, printer: Callable = print):
        self.printer = printer

    def __call__(self, output: str) -> None:
        self.printer(output)
