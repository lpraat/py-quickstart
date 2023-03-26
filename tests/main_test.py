from src.main import CanTalk, Human


def test_human() -> None:
    h: Human = Human("Lorenzo")
    assert isinstance(h, CanTalk)
