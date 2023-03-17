from src.main import Human, CanTalk


def test_human():
    h: CanTalk = Human("Lorenzo")
    assert isinstance(h, CanTalk)
