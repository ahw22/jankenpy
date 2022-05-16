import pytest
from jankenpy import janken


@pytest.mark.parametrize("playerChoice", list(range(3)))
@pytest.mark.parametrize("cpuChoice", list(range(3)))
def test_who_won_all_valid_inputs(playerChoice, cpuChoice):
    # ARRANGE
    # see params

    # ACT
    result = janken.who_won(playerChoice, cpuChoice, "TESTER")

    # ASSERT
    assert result in range(3), "INVALID RESULT"


def test_who_won_all_invalid_inputs():
    # ARRANGE
    # see params

    # ASSERT
    with pytest.raises(IndexError) as e:
        # ACT
        janken.who_won(10, 2.5, "TESTER")

