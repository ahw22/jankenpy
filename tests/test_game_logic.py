import pytest
from jankenpy import janken
from jankenpy.io.InputControllerTUI import TUIInputController
from jankenpy.io.IOController import IOController
from jankenpy.io.OutputControllerTUIPrinter import TUIPrinter


@pytest.mark.parametrize("playerChoice", list(range(3)))
@pytest.mark.parametrize("cpuChoice", list(range(3)))
def test_who_won_all_valid_inputs(playerChoice, cpuChoice):
    # ARRANGE
    # see params
    iocontroller = IOController(TUIInputController(), TUIPrinter())

    # ACT
    result = janken.who_won(playerChoice, cpuChoice, "TESTER", iocontroller)

    # ASSERT
    assert result in range(3), "INVALID RESULT"


def test_who_won_all_invalid_inputs():
    # ARRANGE
    # see params
    iocontroller = IOController(TUIInputController(), TUIPrinter())

    # ASSERT
    with pytest.raises(IndexError) as e:
        # ACT
        janken.who_won(10, 2.5, "TESTER", iocontroller)

