import config
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# логирование информации по работе бота в текстовой файл
logging.basicConfig(filename='log.txt', level=logging.INFO)

# инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# обработка команды start. Простое текстовое сообщение
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await message.answer('Приветик ;) \
		Это тестовый бот с ограниченный функционалом. \
		Доступны три команды \
		/start \
		/help \
		/links')

# обработка команды help. Простое текстовое сообщение
@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
	await message.answer('Здесь краткая информация о работе бота')

# кнопка типа гипер - ссылки, указываем разметку для кнопок, кол-во кнопок в одном ряду
urlkb = InlineKeyboardMarkup(row_width=2)

urlButton1 = InlineKeyboardButton(text='FullStackPython', url='https://www.fullstackpython.com/best-python-resources.html')
urlButton2 = InlineKeyboardButton(text='Pynative', url='https://pynative.com/python/')
urlButton3 = InlineKeyboardButton(text='Qhmit', url='https://www.qhmit.com/python/tutorial/')
urlButton4 = InlineKeyboardButton(text='Overcoder', url='https://overcoder.net')
urlButton5 = InlineKeyboardButton(text='Pythonbooks', url='https://pythonbooks.revolunet.com')
urlButton6 = InlineKeyboardButton(text='Pythoncheatsheet', url='https://www.pythoncheatsheet.org')

urlkb.add(urlButton1, urlButton2, urlButton3, urlButton4, urlButton5, urlButton6)

# обработка команды вызова клавиатуры
@dp.message_handler(commands=['links'])
async def url_command(message: types.Message):
	await message.answer('Полезные ресурсы для Python разработчика: ', reply_markup=urlkb)

# обработка пустых или неправильных команд, удаление неправильной команды пользователя
@dp.message_handler()
async def empty(message: types.Message):
	await message.answer('Нет такой команды')
	await message.delete()

# запуск бота
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)

