import re
from typing import Any, Iterable


def filter_by_state(transactions: list[dict[str, Any]], search_string: str) -> list[dict[str, Any]]:
    """Функция возвращает отсортированный список словарей"""
    new_list = []
    pattern = re.escape(search_string)
    for transaction in transactions:
        state = transaction.get("state", "")
        if isinstance(state, str) and re.search(pattern, state, re.IGNORECASE):
            new_list.append(transaction)
    return new_list


def sort_by_date(list_dicts: Iterable[dict[Any, Any]], keys: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dicts, key=lambda x: x["date"], reverse=keys)
    return sorted_list
