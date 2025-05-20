import pytest
import _4_rotting_oranges as _t

@pytest.mark.parametrize(
    "input, output", [
        pytest.param(
            [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
            4
        ),
    ]
)
def test_solution(input: list[list[int]], output: int):
    ss = _t.Solution()
    
    out = ss.orangesRotting(input)

    assert out == output