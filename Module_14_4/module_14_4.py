from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import asyncio
import sqlite3


from crud_functions import *

initiate_db()




api = '***'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

button_inf = KeyboardButton(text='Информация')
button_calc = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')

kb = ReplyKeyboardMarkup(resize_keyboard=True).row(button_calc, button_inf, button_buy)
# kb.add(button_inf)
# kb.add(button_calc)

kb2 = InlineKeyboardMarkup()
button_calc2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formula = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

kb2.add(button_calc2)
kb2.add(button_formula)

button_product1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_product2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_product3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_product4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

kb_product = InlineKeyboardMarkup(resize_keyboard=True).row(button_product1, button_product2, button_product3,
                                                            button_product4)


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    prod_data=get_all_products()

    for prod in prod_data:
        await message.answer(f'Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[3]}')
        with open(f'Pic/p{prod[0]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_product)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    vol_calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий {vol_calories}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
