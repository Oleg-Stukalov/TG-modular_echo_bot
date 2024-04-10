import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


# Function for bot config and start
async def main() -> None:

    # Load configuration in var config
    config: Config = load_config()

    # Initialize bot and dispatcher
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Skip stored updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())