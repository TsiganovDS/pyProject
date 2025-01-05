from unittest.mock import patch

import pandas as pd

from src.csvread import file_patch, file_patch1, read_csv, read_excel


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
    mock_read_csv.return_value = mock_data

    result = read_csv(file_patch)

    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected
    mock_read_csv.assert_called_once_with(file_patch)


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
    mock_read_excel.return_value = mock_data

    result = read_excel(file_patch1)

    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected
    mock_read_excel.assert_called_once_with(file_patch1)
