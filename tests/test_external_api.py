from typing import Any
from unittest.mock import patch

from src.external_api import API_KEY, currency_conversion


@patch("requests.get")
def test_currency_conversion_success(mock_get: Any) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"conversion_rate": 1.5}  # Возвращаем курс конверсии
    mock_get.return_value.text = "Успех"  # Устанавливаем текст ответа

    transaction = {
        "operationAmount": {"amount": "1000.50", "currency": {"code": "USD"}},
    }

    result = currency_conversion(transaction)

    # Проверяем, что результат соответствует ожидаемому
    expected_result = round(1000.50 * 1.5, 2)  # Ожидаемое значение
    assert result == expected_result

    # Проверяем, что запрос был сделан с правильным URL
    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/RUB",
        headers={"apikey": API_KEY},
    )
