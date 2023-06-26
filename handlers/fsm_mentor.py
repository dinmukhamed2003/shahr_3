from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import keyboards
from config import bot, ADMINs
from database.bot_db import sql_command_insert



class FSM_mentors(StatesGroup):
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and  message.from_user.id in ADMINs:
        await FSM_mentors.name.set()
        await message.answer("Как зовут Ментора?")
    elif message.from_user.id not in ADMINs:
        await message.answer("Вы не являетесь Куратором!!!")
    else:
        await message.reply("Прошу писать в личные сообщения!")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_mentors.next()
    await message.answer("Какое направление у Ментора?", reply_markup=keyboards.direction_markup)

async def load_direction(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['frontend', 'backend', 'android', 'ios', 'ux/ui']:
        await message.answer("Используйте только кнопки!")
    else:
        async with state.proxy() as data:
            data['direction'] = message.text
        await FSM_mentors.next()
        await message.answer("Какой возраст у Ментора?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пишите только числа!")
    elif not 12 <= int(message.text) < 50:
        await message.answer("Не подходит возраст!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSM_mentors.next()
        await message.answer("Какая группа у Ментора?")

async def load_group(message: types.Message, state: FSMContext):
    if not message.text.isalpha:
        await message.answer("Напишите номер группы!")
    else:
        async with state.proxy() as data:
            data['group'] = message.text
        await FSM_mentors.next()
        await message.answer("Все ли данные указаны верно?", reply_markup=keyboards.submit_markup)

async def submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            await sql_command_insert(state)
            await message.answer(f"Информация о менторе: \nИмя: {data['name']};"
                                 f" \nНаправление: {data['direction']} разработчик; \nВозраст: {data['age']}; \nГруппа: {data['group']}.")
            await state.finish()
        elif message.text.lower() == 'заново':
            await FSM_mentors.name.set()
            await message.answer("Как зовут Ментора?")

def register_hanlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSM_mentors.name)
    dp.register_message_handler(load_direction, state=FSM_mentors.direction)
    dp.register_message_handler(load_age, state=FSM_mentors.age)
    dp.register_message_handler(load_group, state=FSM_mentors.group)
    dp.register_message_handler(submit, state=FSM_mentors.submit)