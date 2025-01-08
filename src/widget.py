from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(cart: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах."""
    name_cart = ""
    numer_cart = ""
    cart = str(cart).strip()

    for i in cart:
        if i.isalpha():
            name_cart += i
        elif i.isdigit():
            numer_cart += i

    name_cart = name_cart.strip()

    if len(numer_cart) == 16:
        return str(name_cart + " " + get_mask_card_number(numer_cart))
    elif len(numer_cart) == 20:
        return str(name_cart + " " + get_mask_account(numer_cart))


def get_date(date_sting: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"  и возвращает
    строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    if len(date_sting) == 0:
        raise ValueError("Отсутствует дата")
    date_obj = datetime.fromisoformat(date_sting).date()
    return date_obj.strftime("%d.%m.%Y")
