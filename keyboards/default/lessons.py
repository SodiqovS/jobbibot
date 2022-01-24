from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lesson = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Matematika"),
            KeyboardButton(text="Fizika"),
        ],
    ],
    resize_keyboard=True
)