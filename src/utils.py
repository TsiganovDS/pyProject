import json
import os


def loadtrfrom_json(file_path: str) -> list:
    try:
        with open(file_path, encoding="utf-8") as file:
            try:
                content = json.load(file)
            except json.JSONDecodeError:
                return []
        if not isinstance(content, list):
            return []
    except FileNotFoundError:
        return []
    return content


print(loadtrfrom_json(file_path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")))
file_path = os.path.join(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json"))
content = loadtrfrom_json(file_path)


def sum_transaction(money):
    from src.external_api import currency_conversion

    if money["operationAmount"]["currency"]["code"] == "RUB":
        result = money["operationAmount"]["amount"]
        return float(result)
    else:
        return currency_conversion(money)


for transaction in content:
    rub_amount = sum_transaction(transaction)
    if rub_amount is not None:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')}: Сумма в RUB = {rub_amount}")
    else:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')} не в RUB или данные некорректны.")
