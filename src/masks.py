import logging
import os

path = os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log")


def setup_masks_logger() -> logging.Logger:
    masks_logger = logging.getLogger("masks")
    masks_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(path, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    masks_logger.addHandler(file_handler)
    return masks_logger


masks_logger = setup_masks_logger()


def get_mask_card_number(numer_cart: str) -> str:
    """Функция маскировки номера карты"""
    masks_logger.info("Запуск функции get_mask_card_number")
    if len(str(numer_cart)) != 16:
        masks_logger.error("Неправильный номер карты: %s", numer_cart)
        raise ValueError("Неправильный номер карты")

    return f"{numer_cart[:4]} {numer_cart[4:6]}** **** {numer_cart[12:]}"



def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    masks_logger.info("Запуск функции getmask_account.")
    if not account_number.isdigit() or len(str(account_number)) != 20:
        masks_logger.error("Неправильный номер счета: %s", account_number)
        raise ValueError("Неправильный номер счета")
    return f"**{account_number[-4:]}"
