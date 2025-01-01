import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: dict) -> Any:
    """Функция конвертации"""
    from_convert = transaction["operationAmount"]["currency"]["code"]
    to_convert = "RUB"
    amount = float(transaction["operationAmount"]["amount"])
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_convert}&from={from_convert}&amount={amount}"
    headers = {"apikey": API_KEY}
    r = requests.get(url, headers=headers)
    result = r.json()
    return result
