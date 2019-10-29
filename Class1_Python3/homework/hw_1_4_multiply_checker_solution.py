def multiply(number_1, number_2):
    return number_1 * number_2


def test_multiply():
    assert multiply(1,0) == 0
    assert multiply(1, 10) == 10
    assert multiply(-0.5, 20) == -10


if __name__ == '__main__':
    test_multiply()
    print("Success")


