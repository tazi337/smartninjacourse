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
        return round(value * conversion_rate, 2) # rundet auf 2 Stellen
    except:
        return "Failed to Convert"


# Zeile 2-9 findet die Umrechungszahl heraus
# else, alles andere - z.B. inch - ist nicht möglich
# try: - das wäre die Rechnung, die er versuchen soll
# except: - wenn ein Fehler ausgeworfen worden wäre, dann stürzt mir das programm trotzdem nicht ab


def test_unit_converter():
    assert unit_converter("mile", "km", 1.12) == 1.79
    assert unit_converter("km", "mile", 1) == 0.62
    assert unit_converter("mile", "mile", 1) == 1
    assert unit_converter("km", "km", 1) == 1
    assert unit_converter("mile", "km", "something") == "Failed to Convert"


if __name__ == '__main__':
    test_unit_converter()
