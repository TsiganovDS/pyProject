import re
from collections import Counter

from src.csvread import file_xlxs, read_exc


def filter_transactions(filtered: list[dict], search_string: str) -> list[dict]:
    """Функция для фильтрации списка словарей с операциями на основе строки поиска."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = [
        data for data in filtered if "description" in data and pattern.search(data["description"])
    ]
    return filtered_transactions


transactions = read_exc(file_xlxs)


def count_operations_by_category(transactions: list[dict], categories: str) -> dict[str, int]:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    description_count = Counter()

    for transaction in transactions:
        description = transaction.get("description")
        if description:
            description_count[description] += 1
    result = dict(description_count)
    return result
