from aiogram import executor
import logging
from config import dp
from handlers import commands, callback, extra, admin, fsm_mentor

commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
fsm_mentor.register_hanlers_fsm_mentor(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)