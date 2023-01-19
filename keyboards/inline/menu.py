from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def dyn(text_button):
    a = len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text=text_button[i], callback_data=str(i)) for i in range(0,a)]

    ]
)

def buttons(text_button):
    a=len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=str(text_button[i][1])+str(text_button[i][1]), callback_data=str(i+1)) for i in range(0, a)
            ]
        ]
    )
