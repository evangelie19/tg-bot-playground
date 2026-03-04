import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


def main_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Помощь")
    kb.button(text="Привет")
    kb.button(text="Убрать кнопки")
    kb.adjust(2, 1)  # 2 кнопки в ряд, потом 1
    return kb.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Я живой. Напиши что-нибудь 🙂",
        reply_markup=main_kb()
    )


@dp.message(Command("help"))
@dp.message(F.text == "Помощь")
async def help_cmd(message: Message):
    await message.answer(
        "Команды:\n/start — старт\n/help — помощь\n\nКнопки:\nПомощь — показать это сообщение\nПривет — поздороваться\nУбрать кнопки — спрятать клавиатуру"
    )


@dp.message(F.text == "Привет")
async def hello(message: Message):
    await message.answer("Привет! Отдел Невнятных Решений на связи 🕵️‍♀️")


@dp.message(F.text == "Убрать кнопки")
async def remove_kb(message: Message):
    await message.answer("Ок, убрала кнопки.", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text)
async def echo(message: Message):
    await message.answer(f"Эхо: {message.text}")


async def main():
    if not TOKEN:
        raise RuntimeError("Не найден BOT_TOKEN. Проверь .env (BOT_TOKEN=...)")
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())