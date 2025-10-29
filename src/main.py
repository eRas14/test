import asyncio
import logging
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters.command import Command
from config import BOT_TOKEN
from keyboards.menus import main_menu
from hendlers import hendlers_messages


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

dp.include_routers(hendlers_messages.router)
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

##функция
if __name__ == "__main__":
    asyncio.run(main())
