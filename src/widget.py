def mask_account_card(card_number: str) -> str:
    """Функция маскировки номера карты"""
    return f"{card_number[0:4]} **{card_number[-4:]}"


def get_date(date_: str) -> str:
    """Функция возврата даты"""
    return f"{date_[8:10]}.{date_[5:7]}.{date_[0:4]}"


print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
