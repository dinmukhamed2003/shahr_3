from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp




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


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix='!')
