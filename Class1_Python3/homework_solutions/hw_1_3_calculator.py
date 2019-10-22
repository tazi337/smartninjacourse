def calculator(number_1: float, number_2: float, operation: chr) -> float or None:
    # add your function here
    if operation == "/" and number_2 == 0:
        return None
    try:
        if operation == "+":
            return number_1 + number_2
        elif operation == "-":
            return number_1 - number_2
        elif operation == "*":
            return number_1 * number_2
        elif operation == "/":
            return number_1 / number_2
    except:
        return "Invalid entry"


def test_calculator():
    assert calculator(1, 2, "+") == 3
    assert calculator(1, 2, "-") == -1
    assert calculator(2, 3, "*") == 6
    assert calculator(1, 2, "/") == 0.5
    assert calculator(1, 0, "/") is None
    assert calculator("1", 0, "+") == "Invalid entry"


if __name__ == '__main__':
    test_calculator()
