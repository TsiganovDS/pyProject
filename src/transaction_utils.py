import re

from collections import defaultdict


def filter_transactions(filtered: list[dict], search_string: str) -> list[dict]:
    """ Функция для фильтрации списка словарей с операциями на основе строки поиска."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = [
        data for data in filtered if "description" in data and pattern.search(data["description"])
    ]
    return filtered_transactions


def count_operations_by_category(filtered: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    category_count = defaultdict(int)
    for transaction in filtered:
        description = transaction.get("description", "").lower()
        for category in description:
            if re.search(re.escape(category.lower()), description):
                category_count[category] += 1
    return  dict(category_count)


