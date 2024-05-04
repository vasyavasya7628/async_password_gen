from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from common.k_start import kb_start

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        f"Здравствуйте, я бот генератор паролей.\n Чтобы сгенерировать пароль нажмите кнопку 'Сгенерировать'. \n "
        f"После этого на экран будет выведено 10 паролей.",
        reply_markup=kb_start())
