from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(cart: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах."""
    name_cart = ""
    numer_cart = ""
    list_cart = cart.split()
    for i in list_cart:
        if i.isdigit():
            numer_cart += i
        elif i.isalpha():
            name_cart += i + " "
    if len(numer_cart) == 16:
        return str(name_cart + get_mask_card_number(str(numer_cart)))
    elif len(numer_cart) == 20:
        return str(name_cart + get_mask_account(str(numer_cart)))
    else:
        raise ValueError("Введен неправильный номер")


def get_date(date_sting: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"  и возвращает
    строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    if len(date_sting) == 0:
        raise ValueError("Отсутствует дата")
    date_obj = datetime.fromisoformat(date_sting).date()
    return date_obj.strftime("%d.%m.%Y")
