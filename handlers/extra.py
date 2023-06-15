from aiogram import types, Dispatcher
from config import dp, bot
import random


emoje = ["🎲", "🎯", "🎰", "🎳", "🏀", "⚽️"]

async def game_1(message: types.Message):
    if message.text.startswith("game"):
        random_emoji = random.choice(emoje)
        await bot.send_dice(message.chat.id, emoje)



# @dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    if message.text.isnumeric():
        number = int(message.text)
        squared = number ** 2
        await message.reply(f"Квадрат числа {number}: {squared}")
    else:
        await message.reply(f"Вы написали: {message.text}")





def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(game_1, content_types=['text'])
    dp.register_message_handler(handle_text, content_types=['text'])
