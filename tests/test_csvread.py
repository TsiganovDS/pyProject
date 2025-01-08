from unittest.mock import patch

import pandas as pd

from src.csvread import file_csv, file_xlxs, read_csv, read_exc


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv) -> None:
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
    mock_read_csv.return_value = mock_data

    result = read_csv(file_csv)

    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected
    mock_read_csv.assert_called_once_with(file_csv)


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel) -> None:
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
    mock_read_excel.return_value = mock_data

    result = read_exc(file_xlxs)

    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected
    mock_read_excel.assert_called_once_with(file_xlxs)
