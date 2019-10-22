def guess_number(number: int, secret: int) -> str:
    # add your function here
    return ""


def test_guess_the_number():
    # set secret
    secret = 10

    assert guess_number(1, secret) == ""
    assert guess_number(2, secret) == ""
    assert guess_number("1", secret) == ""
    assert guess_number(-1, secret) == ""


if __name__ == '__main__':
    test_guess_the_number()
