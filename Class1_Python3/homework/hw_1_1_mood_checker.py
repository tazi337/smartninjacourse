def mood_checker(mood: str) -> str:
    # add your function here
    if mood == "happy":
        return "It is great to see you happy!"
    elif mood == "nervous":
        return "Take a deep breath 3 times.!"
    else:
        return "I don't recognize this mood"


def test_mood_checker():
    assert mood_checker("happy") == "It is great to see you happy!"
    assert mood_checker("nervous") == "Take a deep breath 3 times.!"
    assert mood_checker(12) == "I don't recognize this mood"
    assert mood_checker("12") == "I don't recognize this mood"
    assert mood_checker("") == "I don't recognize this mood"

# guard - schützt Code davor ungewollt ausgeführt zu werden.
# name wird in der regel immer mit main benutzt. ist somit eine fixe variable.
if __name__ == '__main__':
    test_mood_checker()
