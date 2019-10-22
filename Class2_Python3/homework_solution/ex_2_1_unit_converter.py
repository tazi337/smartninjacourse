def unit_converter(source_unit: str, target_unit: str, value: float) -> float:
    if source_unit == "mile" and target_unit == "km":
        conversion_rate = 1.6
    elif source_unit == "km" and target_unit == "mile":
        conversion_rate = 1 / 1.6
    elif source_unit == target_unit:
        conversion_rate = 1
    else:
        return "Cannot convert these units"
    try:
        return round(value * conversion_rate, 2)
    except:
        return "Failed to Convert"


def test_unit_converter():
    assert unit_converter("mile", "km", 1.12) == 1.79
    assert unit_converter("km", "mile", 1) == 0.62
    assert unit_converter("mile", "mile", 1) == 1
    assert unit_converter("km", "km", 1) == 1
    assert unit_converter("mile", "km", "something") == "Failed to Convert"


if __name__ == '__main__':
    test_unit_converter()
