import csv
import os

path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")


def read_csv(path: str) -> list:
    rows = []
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


print(read_csv(path))
