import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_mask_card_no_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("7000792289606361098776")


def test_mask_account_no_number_invalid():
    with pytest.raises(ValueError):
        get_mask_account("")


def test_mask_account_number_invalid():
    with pytest.raises(ValueError):
        get_mask_account("70007922896063618758432098776")
