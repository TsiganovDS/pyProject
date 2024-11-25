def mask_account_card(card_number: str) -> str:
    """Функция маскировки номера карты"""
    return f"{card_number[0:4]} {card_number[-4:]}"


print(mask_account_card("Счет 73654108430135874305"))