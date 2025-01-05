import os

import pandas as pd

file_patch = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")


def read_csv(path: str) -> list[dict]:
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


print(read_csv(file_patch))

file_patch1 = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def read_excel(file_path1: str) -> list[dict]:
    df = pd.read_excel(file_path1)
    transactions = df.to_dict(orient="records")
    return transactions


print(read_excel(file_patch1))
