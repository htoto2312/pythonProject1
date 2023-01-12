from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import colors
from loader import dp
from states import Flow

@dp.message_handler(CommandStart, state=Flow.RegisterState)
async def bot_echo(message: types.Message):
    await message.answer(f"tu vvell telefon")

@dp.message_handler(CommandStart)
async def bot_echo(message: types.Message):
    await message.answer(f"we need fone",reply_markup=colors)
