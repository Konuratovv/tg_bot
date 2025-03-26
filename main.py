import os
import dotenv
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('tg_token'))
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('HELLO!')
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())