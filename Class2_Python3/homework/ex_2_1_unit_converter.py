def unit_converter(source_unit: str, target_unit: str, value: float) -> float:
    # write code here
    pass


def test_unit_converter():
    assert unit_converter("mile", "km", 1.12) == 1.79
    assert unit_converter("km", "mile", 1) == 0.62
    assert unit_converter("mile", "mile", 1) == 1
    assert unit_converter("km", "km", 1) == 1
    assert unit_converter("mile", "km", "something") == "Failed to Convert"


if __name__ == '__main__':
    test_unit_converter()
