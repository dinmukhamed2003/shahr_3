from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp, ADMINs
from database.bot_db import sql_command_random
from aiogram.dispatcher.filters import Text
from database.bot_db import sql_command_all, sql_command_delete

# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Ассаламу Алейкум {message.from_user.full_name}")


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message) -> None:
    await bot.send_photo(message.chat.id, photo='https://klike.net/uploads/posts/2018-08/1533804949_5.jpg')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("Следующий вопрос", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Кто основатель Майкрософт?"
    answers = [
        "Макр Цукерберг",
        "Билл Гейтс",
        "Дональд Трамп",
        "Стив Джобс",
        "Илон Маск"
        ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )

async def pin_message(message: types.Message) -> None:
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


async def get_random_user(message: types.Message) -> None:
    random_user = await sql_command_random()
    await message.answer(f"Информация о менторе: \nИмя: {random_user[1]};"
                     f" \nНаправление: {random_user[2]} разработчик; \nВозраст: {random_user[3]}; \nГруппа: {random_user[4]}.")

async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("Вы не являетесь Куратором!!!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(f"Информация о менторе: \nИмя: {user[1]};"
                                 f" \nНаправление: {user[2]} разработчик; \nВозраст: {user[3]}; \nГруппа: {user[4]}.",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"Удалить {user[1]}",
                                                          callback_data=f"delete {user[0]}")
                                 )
            )


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.replace("delete ", ""))
    await callback.answer("Удален с Базы Данных!", show_alert=True)
    await callback.message.delete()



def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(get_random_user, Text(equals="get", ignore_case=True))
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete "))
