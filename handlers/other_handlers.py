from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_en import LEXICON_EN


# Initialize module router
router = Router()

# Handler for any messages except "/start" and "/help" commands
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_EN['no_echo'])