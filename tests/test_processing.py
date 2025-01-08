import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    return [
        {"state": "completed", "date": "2023-01-01"},
        {"state": "completed", "date": "2023-01-15"},
        {"state": "pending", "date": "2023-02-01"},
        {"state": "failed", "date": "2023-03-01"},
    ]


def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, "completed")
    expected = [
        {"state": "completed", "date": "2023-01-01"},
        {"state": "completed", "date": "2023-01-15"},
    ]
    assert result == expected

    result = filter_by_state(sample_transactions, "pending")
    expected = [
        {"state": "pending", "date": "2023-02-01"},
    ]
    assert result == expected

    result = filter_by_state(sample_transactions, "notfound")
    expected = []
    assert result == expected


def test_sort_by_date(sample_transactions):
    result = sort_by_date(sample_transactions, keys=True)
    expected = [
        {"state": "failed", "date": "2023-03-01"},
        {"state": "pending", "date": "2023-02-01"},
        {"state": "completed", "date": "2023-01-15"},
        {"state": "completed", "date": "2023-01-01"},
    ]
    assert result == expected

    result = sort_by_date(sample_transactions, keys=True)
    expected_reversed = [
        {"state": "failed", "date": "2023-03-01"},
        {"state": "pending", "date": "2023-02-01"},
        {"state": "completed", "date": "2023-01-15"},
        {"state": "completed", "date": "2023-01-01"},
    ]
    assert result == expected_reversed
