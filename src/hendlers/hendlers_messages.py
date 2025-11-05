# Хэндлер на команду /start
from aiogram import types, F, Router
from aiogram.filters import Command
from keyboards.menus import main_menu
from aiogram.types import Poll

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n Прошу тебя нажать одну из кнопок", reply_markup=main_menu())

@router.message(Command('poll'))
async def send_regular_poll(message: types.Message):
    await message.answer_poll(
        question="Какой ваш любимый фреймворк?",
        options=["Aiogram", "Pyrogram", "Telethon", "Django"],
        is_anonymous=False,
        allows_multiple_answers=True
    )

@router.message(Command("quiz"))
async def send_quiz_poll(message: types.Message):
    await message.answer_poll(
        question="Каккой из этих героев ловкач?",
        options=["Спирит Брейкер", "Некрофос", "инвокер", "Урса"],
        type="quiz",
        correct_option_id=3,  # Урса
        explanation="Правильно! Урса герой ловкач",
        reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True)

    )

@router.message(F.text.lower() == "левая кнопка")
async def right_choice(message: types.Message):
    await message.answer("Вы нажали правую кнопку\n Начать заново /start", reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))

@router.message(F.text.lower() == "правая кнопка")
async def right_choice(message: types.Message):
    await message.answer("Вы нажали правую кнопку\n Начать заново /start",reply_markup=types.ReplyKeyboardRemove(remove_keyboard=True))

@router.message()
async def wrong_button(message: types.Message):
    await message.answer("Пожалуйста выберите одну из кнопок!")