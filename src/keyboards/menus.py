from aiogram import types

def main_menu() -> list:
    buttons_in_main_menu = [
        [
            types.KeyboardButton(text="Правая кнопка"),
            types.KeyboardButton(text="Левая кнопка")
        ]
    ]

    return types.ReplyKeyboardMarkup(keyboard=buttons_in_main_menu, resize_keyboard=True)