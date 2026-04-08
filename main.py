import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F  # Импортируем F
from aiogram.filters.command import Command

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("tg_token"))
dp = Dispatcher()
SECRET_WORD = os.getenv("SECRET_WORD", "сюрприз")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"О привет, {message.from_user.full_name}!")


@dp.message(Command("help"))
async def help_user(message: types.Message):
    await message.answer(
        "Ничего интересного, я пока простой эхо-бот, но я развиваюсь. Ждите дальнейших обновлений. А и кстати тут есть секретное слово, попробуйте его отгадать"
    )


@dp.message(F.text == SECRET_WORD)
async def secret_word_handler(message: types.Message):
    await message.answer("О! Вы нашли секретное слово! 🎉")


@dp.message(F.text)
async def echo_handler(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
