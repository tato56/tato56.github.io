import asyncio
from aiogram import Bot, Dispatcher, executor

loop = asyncio.new_event_loop()
bot = Bot('6172402507:AAGn6IemgyYmqNF-aX-09vXXvwrX0XXaLxA', parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
