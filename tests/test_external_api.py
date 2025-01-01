from unittest.mock import patch
from src.external_api import currency_conversion, API_KEY


@patch("requests.get")
def test_currency_conversion_success(mock_get):
    # Проверяем ответ от API
    mock_get.return_value.json.return_value = {"result": 1000.0}


    transaction = {"operationAmount": {"amount": "1000.50", "currency": {"code": "USD"}}}


    result = currency_conversion(transaction)
    assert {'result': 1000.0}['result'] == 1000.0


    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000.5",
        headers={"apikey": API_KEY},
    )


