def fizzbuzz_line(eingabe: int) -> str:
    if eingabe % 5 == 0 and eingabe % 3 == 0:
        return "fizzbuzz"
    elif eingabe % 5 == 0:
        return "buzz"
    elif eingabe % 3 == 0:
        return "fizz"
    else:
        return str(eingabe)
    return


def test_fizzbuzz_line():
    assert fizzbuzz_line(1) == "1"
    assert fizzbuzz_line(3) == "fizz"
    assert fizzbuzz_line(5) == "buzz"
    assert fizzbuzz_line(15) == "fizzbuzz"
    assert fizzbuzz_line(-3) == "fizz"


if __name__ == '__main__':
    test_fizzbuzz_line()
