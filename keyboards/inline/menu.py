from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def dyn(text_button):
    a = len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text=text_button[i], callback_data=str(i)) for i in range(0,a)]

    ]
)


