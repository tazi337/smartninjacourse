def calculator(number_1: float, number_2: float, operation: chr) -> float or None:
    # add your function here
    return 0


def test_calculator():
    assert calculator(1, 2, "+") == 3
    assert calculator(1, 2, "-") == -1
    assert calculator(2, 3, "*") == 6
    assert calculator(1, 2, "/") == 0.5
    assert calculator(1, 0, "/") is None


if __name__ == '__main__':
    test_calculator()
