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


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    masks_logger.info("Запуск функции get_mask_card_number")
    if len(str(card_number)) != 16:
        masks_logger.error("Неправильный номер карты: %s", card_number)
        raise ValueError("Неправильный номер карты")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    masks_logger.info("Запуск функции get_mask_account.")
    if len(str(account_number)) != 20:
        masks_logger.error("Неправильный номер счета: %s", account_number)
        raise ValueError("Неправильный номер счета")
    masked_account = f"** {account_number[-4:]}"
    return masked_account


try:
    masks_logger.info(f"Замаскированный номер карты: {get_mask_card_number("7000792289606361")}")
    masks_logger.info(f"Замаскированный номер счета: {get_mask_account("22425621641834121234")}")
except ValueError as e:
    masks_logger.exception("Ошибка: %s", e)
