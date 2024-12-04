from typing import Iterable, Any


def filter_by_state(dictionaries: Iterable[dict[Any, Any]], state: Any="EXECUTED") -> dict[Any, Any]:
    """Функция возвращает отсортированный список словарей"""
    dictionary = []
    for dict_ in dictionaries:
        if dict_["state"] == "EXECUTED":
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


def sort_by_date(list_dicts: Iterable[dict[Any, Any]], reverse: bool = True) -> dict[Any, Any]:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(list_dicts, key=lambda x: x["date"], reverse=reverse)
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