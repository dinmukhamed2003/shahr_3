from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Ассаламу Алейкум {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Самое большое государство в мире?"
    answers = [
        "США",
        "Китай",
        "Россия",
        "Канада",
        "Египет",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
    )


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message) -> None:
    await bot.send_photo(message.chat.id, photo='https://klike.net/uploads/posts/2018-08/1533804949_5.jpg')



@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    if message.text.isnumeric():
        number = int(message.text)
        squared = number ** 2
        await message.reply(f"Квадрат числа {number}: {squared}")
    else:
        await message.reply(f"Вы написали: {message.text}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)