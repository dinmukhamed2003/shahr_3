from aiogram import executor
import logging
from config import dp
from handlers import commands, callback, extra, fsm_mentor, notifications
from database.bot_db import sql_create
import asyncio


async def on_startup(_):
    sql_create()
    asyncio.create_task(notifications.scheduler())


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
fsm_mentor.register_hanlers_fsm_mentor(dp)
extra.register_handlers_extra(dp)
notifications.register_handlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)