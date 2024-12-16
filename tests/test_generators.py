from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency() -> None:
    generator = filter_by_currency(transactions)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_not_list() -> None:
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_not_currency() -> None:
    generator = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions() -> None:
    a = transaction_descriptions(transactions)
    assert next(a) == "Перевод организации"


@pytest.mark.parametrize("index, expected", [(0, "Перевод организации"), (1, "Перевод со счета на счет")])
def test_transaction_descriptions_3(index: Any, expected: Any) -> None:
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


@pytest.fixture
def number_generator() -> list:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


@pytest.fixture
def transaction_des() -> list:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_card_number_generator() -> None:
    numer = card_number_generator(95, 96)
    assert next(numer) == "0000 0000 0000 0095"


def test_card_number_generator_beginning() -> None:
    numer = card_number_generator(0, 1)
    assert next(numer) == "0000 0000 0000 0000"


def test_card_number_generator_end() -> None:
    numer = card_number_generator(9999999999999999, 9999999999999999)
    assert next(numer) == "9999 9999 9999 9999"
