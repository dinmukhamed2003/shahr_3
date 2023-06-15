from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("Следующий вопрос", callback_data="next_button_2")
    markup.add(next_button)
    question = "Самое большое государство в мире?"
    answers = [
        "США",
        "Китай",
        "Россия",
        "Канада",
        "Египет",
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("Следующий вопрос", callback_data="next_button_3")
    markup.add(next_button)
    question = "Самая длинная река в мире?"
    answers = [
        "Нил",
        "Амозонка",
        "Чуй",
        "Янцзы",
        "Миссури",
    ]

    await callback.message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )

async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer("Ты ответил на все вопросы!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text="next_button_3")