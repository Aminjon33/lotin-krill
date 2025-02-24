import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from state import Registor,Shop, computers
from aiogram.fsm.state import State, StatesGroup
from urllib.parse import urlparse
from aiogram.types import ReplyKeyboardRemove
from lotin_kiril import transliter



TOKEN = ""
ADMIN_ID = ""

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz"


@dp.startup()
async def bot_start():
    await bot.send_message(chat_id=7478200510, text="Botimiz ishga tushdi! /start tugmasini bosing")

@dp.shutdown()
async def bot_start():
    await bot.send_message(chat_id=7478200510, text="Botimiz to'xtadi! Xayr")

@dp.message(F.text == "About us")
async def About_us(message:Message):
    await message.answer("Bu bot sizga savdo boti sifatida xizmat qila oladi !")

@dp.message(F.text)
async def kiril_lotin(message:Message):
    text = transliter(message.text)
    await message.answer(text)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
