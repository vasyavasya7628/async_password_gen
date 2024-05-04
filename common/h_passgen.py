import asyncio
import random
import string

from aiogram import F, Router
from aiogram.types import Message

from common.k_start import kb_start
from res import Res

passgen_router = Router()


@passgen_router.message(F.text.startswith('🔏'))
async def generate(message: Message):
    passwords = await generate_passwords()
    await message.answer(f"{'\n'.join(passwords)}",
                         reply_markup=kb_start())


async def password_generator():
    letters = string.ascii_letters
    numbers = string.digits

    password_digit = random.choice(numbers)
    password_symbol = random.choice(Res.SYMBOLS.value)

    all_chars = letters + numbers + Res.SYMBOLS.value
    all_chars = [password_digit] + random.sample(all_chars, 7) + [password_symbol]

    random.shuffle(all_chars)
    password = "".join(all_chars)

    return password


async def generate_passwords():
    tasks = [password_generator() for _ in range(8)]
    passwords = await asyncio.gather(*tasks)
    return passwords
