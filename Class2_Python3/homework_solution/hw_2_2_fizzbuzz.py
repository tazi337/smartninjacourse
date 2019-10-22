def fizzbuzz_line(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return f"{num}"


def test_fizzbuzz_line():
    assert fizzbuzz_line(1) == "1"
    assert fizzbuzz_line(3) == "fizz"
    assert fizzbuzz_line(5) == "buzz"
    assert fizzbuzz_line(15) == "fizzbuzz"
    assert fizzbuzz_line(-3) == "fizz"


if __name__ == '__main__':
    test_fizzbuzz_line()
