from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует вызов функции и ее результат в файл или на консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
                    print(log_message)
            else:
                print(log_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> float:
    return x + y


my_function(1, 2)
