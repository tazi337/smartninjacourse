def mood_checker(mood: str) -> str:
    # add your function here
    if mood == "happy":
        answer = "It is great to see you happy!"
    elif mood == "nervous":
        answer = "Take a deep breath 3 times."
    else:
        answer = "I don't recognize this mood."
    return answer


def test_mood_checker():
    assert mood_checker("happy") == "It is great to see you happy!"
    assert mood_checker("nervous") == "Take a deep breath 3 times.!"
    assert mood_checker(12) == "I don't recognize this mood"
    assert mood_checker("12") == "I don't recognize this mood"
    assert mood_checker("") == "I don't recognize this mood"


if __name__ == '__main__':
    test_mood_checker()
