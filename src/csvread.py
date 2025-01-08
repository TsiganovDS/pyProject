import csv
import os

import pandas as pd

file_csv = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")


def read_csv(file_csv: str) -> list[dict]:
    result = []
    try:
        with open(file_csv, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            for row in reader:
                if len(row) != len(header):
                    raise ValueError(f"Неверное количество колонок в строке: {row}")

                row_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                result.append(row_dict)
    except FileNotFoundError:
        print(f"Файл {file_csv} не найден.")
    except ValueError as ve:
        print(f"Ошибка данных: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


file_xlxs = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def read_exc(file_xlxs: str) -> list[dict]:
    df = pd.read_excel(file_xlxs)
    result = df.apply(
        lambda row: {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        },
        axis=1,
    ).tolist()
    return result
