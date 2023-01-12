from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
colors=ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='share namber', request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
