import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.basic_handlers import router as basic_router
from handlers.menu_handler import router as menu_router

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("tg_token"))
dp = Dispatcher()


async def main():
    dp.include_router(menu_router)
    dp.include_router(basic_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
