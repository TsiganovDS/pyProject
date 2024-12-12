import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account_score() -> None:
    assert mask_account_card("64686473678894779589") == "**9589"


@pytest.mark.parametrize(
    "numer, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990 9221 1366 5229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account(numer: str, expected: str) -> None:
    assert mask_account_card(numer) == expected


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro 159683786870519999")


def test_mask_account_score_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Счет 353830334744478958473560")


def test_mask_account_card_zero_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        get_date("")
