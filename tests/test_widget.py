import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # Тест для карт
    assert mask_account_card("Visa 1234567812345678") == "Visa 1234 56** **** 5678"
    assert mask_account_card("MasterCard 8765432187654321") == "MasterCard 8765 43** **** 4321"

    # Тест для счетов
    assert mask_account_card("Account 12345678901234567890") == "Account **7890"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-01-01T00:00:00.000000") == "01.01.2024"

    # Тест на обработку пустой строки
    with pytest.raises(ValueError, match="Отсутствует дата"):
        get_date("")
