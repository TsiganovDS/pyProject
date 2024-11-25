def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    return f"**{account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("22425621641834121234"))
