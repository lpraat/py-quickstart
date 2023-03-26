from src.main import CanTalk, Human


def test_human() -> None:
    h: int = Human("Lorenzo")
    assert isinstance(h, CanTalk)
