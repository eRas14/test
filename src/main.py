import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import os
from dotenv import load_dotenv


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Выгрузка переменных
load_dotenv()

# Объект бота
bot = Bot(token=os.getenv('BOT_TOKEN'))
# Диспетчер
dp = Dispatcher()

buttons = [
    [
        types.KeyboardButton(text="Правая кнопка"),
        types.KeyboardButton(text="Левая кнопка")
    ]
]

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    buttons_in_menu = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(f"Привет, {message.from_user.full_name}!\n Прошу тебя нажать одну из кнопок", reply_markup=buttons_in_menu)

@dp.message(F.text.lower() == "правая кнопка")
async def right_choice(message: types.Message):
    await message.answer("Вы нажали правую кнопку\n Начать заново /start", reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))

@dp.message(F.text.lower() == "левая кнопка")
async def right_choice(message: types.Message):
    
    await message.answer("Вы нажали левую кнопку\n Начать заново /start",reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))


@dp.message()
async def wrong_button(message: types.Message):
    await message.answer("Пожалуйста выберите одну из кнопок")




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

##функция
if __name__ == "__main__":
    asyncio.run(main())
