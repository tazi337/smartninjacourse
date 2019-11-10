def unit_converter(source_unit: str, target_unit: str, value: float) -> float:
    try:
        if source_unit == "mile" and target_unit == "km":
            return round(value * 1.60, 2)
        elif source_unit == "km" and target_unit == "mile":
            return round(value * 1/1.60, 2)
        elif source_unit == "mile" and target_unit == "mile":
            return round(value * 1, 2)
        elif source_unit == "km" and target_unit == "km":
            return round(value * 1, 2)
        else:
            return "Cannot convert these units - please insert km or miles"
    except: return "Failed to Convert"


# try and except wäre hier auch möglich, dafür muss aber die if-anweisung komplett im try stehen und danach erst das except

def test_unit_converter():
    assert unit_converter("mile", "km", 1.12) == 1.79
    assert unit_converter("km", "mile", 1) == 0.62
    assert unit_converter("mile", "mile", 1) == 1
    assert unit_converter("km", "km", 1) == 1
    assert unit_converter("mile", "km", "something") == "Failed to Convert"


if __name__ == '__main__':
    test_unit_converter()



