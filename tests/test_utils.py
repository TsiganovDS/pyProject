from src.utils import loadtrfrom_json, file_path

from unittest.mock import patch


@patch("json.load")
def test_loadtrfrom_json(mock_load):
    """Проверка ожидаемого результата"""
    mock_load.return_value = [1, 2, 3]
    result = loadtrfrom_json(file_path)
    assert result == [1, 2, 3], f"Expected [1, 2, 3], but got {result}"
