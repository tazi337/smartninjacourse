def guess_number(number: int, secret: int) -> str:
    # add your function here
    if number == secret:
        return f"You've guessed it - congratulations! It's number {secret}."
    else:
        return f"Sorry, your guess is not correct... The secret number is not {number}"


def test_guess_the_number():
    # set secret
    secret = 10

    assert guess_number(10, secret) == f"You've guessed it - congratulations! It's number {secret}."
    assert guess_number(2, secret) == f"Sorry, your guess is not correct... The secret number is not {2}"
    assert guess_number("1", secret) == f"Sorry, your guess is not correct... The secret number is not {1}"
    assert guess_number(-1, secret) == f"Sorry, your guess is not correct... The secret number is not {-1}"


if __name__ == '__main__':
    test_guess_the_number()
