import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Tokeningizni quyidagi qo'shtirnoq ichiga yozing
TOKEN = "8818601883:AAFy0y2MIFY1IV0JokaWKCPKjXZmoqwPfm8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom! Botim Render'da muvaffaqiyatli ishga tushdi! 🚀")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
