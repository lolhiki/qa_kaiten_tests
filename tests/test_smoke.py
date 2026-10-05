def test_smoke():
    """Проверка: pytest вообще запускается и базовые операции работают."""
    assert 1 + 1 == 2


def test_string_operations():
    """Проверка: базовые строковые операции работают."""
    assert "kaiten".upper() == "KAITEN"
    assert "qa".replace("a", "A") == "qA"
