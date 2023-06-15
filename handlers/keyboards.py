from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    # row_width=1
)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
)

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("Frontend"),
    KeyboardButton("Backend"),
    KeyboardButton("Android"),
    KeyboardButton("IOS"),
    KeyboardButton("UX/UI"),
)