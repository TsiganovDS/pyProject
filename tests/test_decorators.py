from typing import Any

from src.decorators import log


def test_log_correct(capsys: Any) -> None:
    # Проверка корректного выполнения функции
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok\n" in captured.out


def test_log_different_types_str(capsys: Any) -> None:
    # Проверка ошибки: missing 2 required positional arguments: 'x' and 'y'.
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    try:
        my_function("a", "b")
    except TypeError:
        captured = capsys.readouterr()
        assert "my_function error: " in captured.out


def test_log_lack_argument(capsys: Any) -> None:
    # Проверка ошибки: missing 1 required positional argument: 'y'.
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    try:
        my_function(
            1,
        )
    except TypeError:
        captured = capsys.readouterr()
        assert "my_function error: " in captured.out


def test_log_different_types_argument(capsys: Any) -> None:
    # Проверка ошибки: unsupported operand type(s) for +: 'int' and 'str'.
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    try:
        my_function(1, "")
    except TypeError:
        captured = capsys.readouterr()
        assert "my_function error: " in captured.out


def test_log_different_types_no_argument(capsys: Any) -> None:
    # Проверка ошибки: missing 2 required positional arguments: 'x' and 'y'
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    try:
        my_function()
    except TypeError:
        captured = capsys.readouterr()
        assert "my_function error: " in captured.out
