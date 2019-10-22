def fizzbuzz_line(num: int) -> str:
    # write your code here
    pass


def test_fizzbuzz_line():
    assert fizzbuzz_line(1) == "1"
    assert fizzbuzz_line(3) == "fizz"
    assert fizzbuzz_line(5) == "buzz"
    assert fizzbuzz_line(15) == "fizzbuzz"
    assert fizzbuzz_line(-3) == "fizz"


if __name__ == '__main__':
    test_fizzbuzz_line()
