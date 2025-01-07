import json
import csv
import os
import re

from src.processing import filter_by_state, sort_by_date
from src.transaction_utils import count_operations_by_category, filter_transactions

from src.csvread import read_csv, file_csv, read_exc, file_xlxs
from src.utils import loadtrfrom_json, file_json
from src.widget import mask_account_card, get_date


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")
    if choice == '1':
        transactions = loadtrfrom_json(file_json)
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        transactions = read_csv(file_csv)
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        transactions = read_exc(file_xlxs)
        print("Для обработки выбран XLSX-файл.")

    print("Введите статус, по которому необходимо выполнить фильтрацию."
        " Доступные для фильтрования статусы: EXECUTED, CANCELED, PENDING\nПользователь: ")

    while True:
        search_string = input()
        if search_string.upper() in ["CANCELED", "PENDING", "EXECUTED"]:
            break
        else:
            print(f"Статус операции {search_string} недоступен.")
            continue
    filtered = filter_by_state(transactions, search_string)

    print("\nОтсортировать операции по дате? Да/Нет")
    while True:
        filter_by_date = input()
        if filter_by_date.lower() == "да":
            print("\nОтсортировать по возрастанию или по убыванию?")
            reverse = input()
            if reverse.lower() == "по убыванию":
                reverse_date = True
            else:
                reverse_date = False
            filtered = sort_by_date(filtered, reverse_date)
            break
        elif filter_by_date.lower() == "нет":
            break
        else:
            continue

    print("\nВыводить только рублевые тразакции? Да/Нет")
    while True:
        data_rub = input()
        if data_rub.lower() == "да" and int(choice) == 1:
            filtered = list(
                filter(lambda x: x.get("operationAmount").get("currency").get("code") == "RUB", filtered))
            break
        elif data_rub.lower() == "да" and int(choice) == 2:
            filtered = list(filter(lambda x: x.get("currency_code") == "RUB", filtered))
            break
        elif data_rub.lower() == "да" and int(choice) == 3:
            filtered = list(filter(lambda x: x.get("currency_code") == "RUB", filtered))
            break
        elif data_rub.lower() == "нет":
            break
        else:
            continue

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        filter_by_word = input()
        if filter_by_word.lower() == "да":
            print("\nВведите слово")
            word = input()
            filtered = filter_transactions(filtered, word)
            break
        if filter_by_word.lower() == "нет":
            break
        else:
            continue

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered)}\n")
        for transaction in filtered:
            date = get_date(transaction.get("date"))
            print(f"{date} {transaction.get("description")}")
            account_from = ""
            if transaction.get("from"):
                account_from = (mask_account_card(transaction.get("from")))
            account_to = mask_account_card(transaction.get("to"))
            print(account_from, " -> ", account_to)
            if int(choice) == 2 or int(choice) == 3:
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]
            else:
                amount = transaction.get("operationAmount").get("amount")
                currency = transaction.get("operationAmount").get("currency").get("name")
            print(f"Сумма: {amount} {currency}\n")


main()







