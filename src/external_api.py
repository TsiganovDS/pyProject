import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: dict) -> float:
    """Функция конвертации"""
    have = transaction["operationAmount"]["currency"]["code"]
    want = "RUB"
    amount = float(transaction["operationAmount"]["amount"])
    api_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{have}/{want}"
    response = requests.get(api_url, headers={"apikey": API_KEY})
    if response.status_code == requests.codes.ok:  # Успешный ответ
        result = response.json()
        if "conversion_rate" in result:
            conversion_rate = result["conversion_rate"]
            converted_amount = round(amount * conversion_rate, 2)
            return float(converted_amount)
        elif response.status_code != 200:
            raise ValueError(f"Ошибка API: {response.status_code} - {response.text}")
        else:
            raise ValueError("Ключ 'conversion_rate' отсутствует в ответе API.")
