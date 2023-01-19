from distutils.cmd import Command
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import colors
from loader import dp, db
from states import Flow
from keyboards.inline import dyn, buttons




@dp.message_handler(commands=['start'], state=Flow.RegisterState)
async def bot_echo (message: types.Message):
    await message.answer (f"You've already shared your phone number.")

@dp.message_handler(conmands=['start'])
async def bot_echo (message: types.Message):
    await message.answer (f"For using our bot, you need to share your phone number first.", reply_markup=colors)

@dp.message_handler(content_Types=types.ContentTypes.CONTACT)
async def bot_echo (message: types.Message):
    if message.contact.user_id!=message.from_id:
        await message.answer(f"Wrong data. Try again.")
    else:

        await Flow.RegisterState.set()
        await message.answer(f'Welcome, {message.from_user.full_name}!')
        await db.add_user(message.contact.user_id, message.contact.phone_number)
@dp.message_handler(state=Flow.RegisterState,commands=['Data'])
async def bot_echo(message: types.Message):
    result=await db.get_users()
    a=''
    for i in result:
        a+=f'id: {i[0]}, phone: {i[1]}.\n'
    await message.answer(text=a, reply_markup=buttons(result))













#@dp.message_handler(content_types=types.ContentTypes.CONTACT)
#async def bot_echo (message: types.Message):
 #   if message.contact.user_id != message.from_id:
  #      await message.answer (f"Wrong data. Try again.")
   # else:
    #    await Flow.RegisterState.set()
     #   await message.answer (f"Welcome {message.from_user.full_name}!")
      #  print(message.contact.phone_number)



















text_button=[
    ['Yes', 'No'],
    ['Banana', 'Bread', 'Soap', 'Plants', 'Chocolate'],
    ['Chocolate', 'Icecream', 'Cookie'],
    ['Winter','Spring','Summer', 'Autumn']
]

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def bot_echo(message: types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer('errrrrrrrrroooooooorrrrrrrrr')
    else:
        await Flow.RegisterState.set()
        await message.answer(f'Welcome {message.from_user.full_name}:\n'
                             f'It`s time trash your monet. press yes', reply_markup=dyn(text_button[0]))



@dp.callback_query_handler(text='0', state=Flow.RegisterState)
async def choose_yes(call: types.CallbackQuery):
    await Flow.Pickfruit.set()
    await call.message.answer(f'pick fruit', reply_markup=dyn(text_button[1]))

@dp.callback_query_handler(text='1', state=Flow.RegisterState)
async def choose_no(call: types.CallbackQuery):
    await call.message.answer(f'welllll')



@dp.callback_query_handler(text='0', state=Flow.Pickfruit)
async def second_choose(call: types.CallbackQuery):
    await Flow.Pickseason.set()
    await call.message.answer(f'pick sweet', reply_markup=dyn(text_button[2]))

@dp.callback_query_handler(text='1', state=Flow.Pickseason)
async def third_choose(call: types.CallbackQuery):
    await Flow.FinishedChoosing.set()
    await call.message.answer(f'pick season', reply_markup=dyn(text_button[3]))

@dp.callback_query_handler(text='1', state=Flow.FinishedChoosing)
async def finished_choosing(call: types.CallbackQuery):
    await Flow.FinishedChoosing.set()
    await call.message.answer(f'thenks ')


