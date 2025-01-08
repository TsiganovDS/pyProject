import json
import logging
import os

patch = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")
file_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def setup_utils_logger() -> logging.Logger:
    utils_logger = logging.getLogger("utils")
    utils_logger.setLevel(logging.DEBUG)
    utils_handler = logging.FileHandler(patch, mode="w", encoding="utf-8")
    utils_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    utils_logger.addHandler(utils_handler)
    return utils_logger


utils_logger = setup_utils_logger()


def loadtrfrom_json(file_json: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        utils_logger.info("Запуск функции loadtrfrom_json.")
        with open(file_json, encoding="utf-8") as file:
            try:
                content = json.load(file)
            except json.JSONDecodeError:
                return []
        if not isinstance(content, list):
            return []
    except FileNotFoundError:
        return []
    return content


utils_logger.info(loadtrfrom_json(file_json))
# content = loadtrfrom_json(file_json)


def sum_transaction(money: dict) -> float:
    utils_logger.info("Запуск функции sum_transaction")
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    from src.external_api import currency_conversion

    if money["operationAmount"]["currency"]["code"] == "RUB":
        result = money["operationAmount"]["amount"]
        return float(result)
    else:
        return currency_conversion(money)


# for transaction in content:
#    amount = sum_transaction(transaction)
#    if amount is not None:
#      utils_logger.info(f"Транзакция ID {transaction.get('id', 'неизвестный ID')}: Сумма в RUB = {amount}")
#   else:
#       utils_logger.info(f"Транзакция ID {transaction.get('id', 'неизвестный ID')} не в RUB или данные некорректны.")
