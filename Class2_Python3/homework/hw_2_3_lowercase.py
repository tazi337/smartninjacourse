def lowercase(text: str) -> str:
    # add your function here
    return text.lower()


def test_lowercase():
    assert lowercase("hi") == "hi"
    assert lowercase("my Bread") == "my bread"
    assert lowercase("DoNe!") == "done!"


if __name__ == '__main__':
    test_lowercase()
