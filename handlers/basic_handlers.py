import os
from dotenv import load_dotenv
from aiogram import types, F, Router
from aiogram.filters.command import Command

load_dotenv()

router = Router()
SECRET_WORD = os.getenv("SECRET_WORD", "сюрприз")


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"О привет, {message.from_user.full_name}!")


@router.message(Command("help"))
async def help_user(message: types.Message):
    await message.answer(
        "Ничего интересного, я пока простой эхо-бот, но я развиваюсь. Ждите дальнейших обновлений. А и кстати тут есть секретное слово, попробуйте его отгадать"
    )


@router.message(F.text == SECRET_WORD)
async def secret_word_handler(message: types.Message):
    await message.answer("О! Вы нашли секретное слово! 🎉")


@router.message(F.text)
async def echo_handler(message: types.Message):
    await message.answer(f"Вы сказали: {message.text}")


@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer(f"Вы отправили фото, но я пока не умею их обрабатывать")


@router.message(F.sticker)
async def sticker_handler(message: types.Message):
    await message.answer(f"Наверное классный стикер, жаль что я не умею их обрабатывать((")