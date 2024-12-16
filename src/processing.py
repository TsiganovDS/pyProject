from typing import Any, Iterable


def filter_by_state(dictionaries: Iterable[dict[Any, Any]], key: str = "EXECUTED") -> list:
    """Функция возвращает отсортированный список словарей"""
    dictionary = []
    for i in dictionaries:
        if not i.get("state"):
            raise ValueError("Отсутствует ключ для фильтра")
    for dict_ in dictionaries:
        if dict_["state"] == key:
            dictionary.append(dict_)
    return dictionary


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(list_dicts: Iterable[dict[Any, Any]], keys: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dicts, key=lambda x: x["date"], reverse=keys)
    return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
