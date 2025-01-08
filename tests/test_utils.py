from typing import Any
from unittest.mock import patch

from src.utils import file_json, loadtrfrom_json


@patch("json.load")
def test_loadtrfrom_json(mock_load: Any) -> None:
    """Проверка ожидаемого результата"""
    mock_load.return_value = [1, 2, 3]
    result = loadtrfrom_json(file_json)
    assert result == [1, 2, 3], f"Expected [1, 2, 3], but got {result}"
