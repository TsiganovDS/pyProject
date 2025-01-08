from src.transaction_utils import filter_transactions

from src.transaction_utils import count_operations_by_category


mock_transactions = [
    {
        "date": "2023-01-01",
        "from": "1234567890123456",
        "to": "9876543210987654",
        "description": "Перевод организации",
        "operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}},
    },
    {
        "date": "2023-01-02",
        "from": "1234567890123456",
        "to": "1111222233334444",
        "description": "Покупка в магазине",
        "operationAmount": {"amount": "500.00", "currency": {"code": "RUB"}},
    },
    {
        "date": "2023-01-03",
        "from": "1234567890123456",
        "to": "5555666677778888",
        "description": "Перевод организации",
        "operationAmount": {"amount": "1500.00", "currency": {"code": "RUB"}},
    },
]


def testfiltertransactions():
    search_string = "Перевод организации"
    result = filter_transactions(mock_transactions, search_string)

    assert len(result) == 2
    assert all("Перевод организации" in transaction["description"] for transaction in result)

    search_string = "Покупка в магазине"
    result = filter_transactions(mock_transactions, search_string)

    assert len(result) == 1
    assert result[0]["description"] == "Покупка в магазине"

    search_string = "Неизвестная операция"
    result = filter_transactions(mock_transactions, search_string)

    assert len(result) == 0


def test_count_operations_by_category() -> None:
    result = count_operations_by_category(mock_transactions, "description")
    assert result["Перевод организации"] == 2
    assert result["Покупка в магазине"] == 1
    assert result.get("Неизвестная операция", 0) == 0
