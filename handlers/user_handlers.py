from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_en import LEXICON_EN


# Handler for /start command
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Handler for /help command
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])