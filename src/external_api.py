import requests


def tranzaction() -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": 1, "from": "EUR", "to": "RUB"}
    headers = {"apikey": ""}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        print(f"Ошибка: {response.status_code}")
        return 0.0


print(tranzaction())
