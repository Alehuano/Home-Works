# В данном модуле использовалась библиотека aiogram 3.xx
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio

api = '***'
bot = Bot(token=api)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message):
    print('Привет! Я бот, помогающий твоему здоровью.')


@dp.message()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    asyncio.run(main())
