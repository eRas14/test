import asyncio
import logging
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters.command import Command
from config import BOT_TOKEN
from keyboards.menus import main_menu


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n Прошу тебя нажать одну из кнопок", reply_markup=main_menu())

@dp.message(F.text.lower() == "левая кнопка")
async def right_choice(message: types.Message):
    await message.answer("Вы нажали правую кнопку\n Начать заново /start", reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))

@dp.message(F.text.lower() == "правая кнопка")
async def right_choice(message: types.Message):
    await message.answer("Вы нажали правую кнопку\n Начать заново /start",reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))

@dp.message()
async def wrong_button(message: types.Message):
    await message.answer("Пожалуйста выберите одну из кнопок")




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

##функция
if __name__ == "__main__":
    asyncio.run(main())
