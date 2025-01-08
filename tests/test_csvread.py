from unittest.mock import patch
import pandas as pd
from src.csvread import read_exc


def test_read_exc():
    # Создаем DataFrame для имитации чтения из Excel
    mock_data = {
        "id": [650703],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [1000],
        "currency_name": ["RUB"],
        "currency_code": ["RUB"],
        "description": ["Transaction description"],
        "from": ["Sender"],
        "to": ["Receiver"],
    }

    df = pd.DataFrame(mock_data)

    # Патчим метод read_excel для возвращения нашего DataFrame
    with patch("pandas.read_excel", return_value=df, sep=";"):
        result = read_exc("mock_file.xlsx")

        expected_result = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {
                    "amount": 1000,
                    "currency": {
                        "name": "RUB",
                        "code": "RUB",
                    },
                },
                "description": "Transaction description",
                "from": "Sender",
                "to": "Receiver",
            }
        ]

        assert result == expected_result
