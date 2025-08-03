import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands, alerts, charts, history, conversions, settings
from scheduler import start_scheduler
from database import init_db

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7208894894:AAEatAs18BWXinxYKNwwRTln9XU7q0x651o"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    init_db()  # Initialize SQLite database
    dp.include_routers(
        commands.router,
        alerts.router,
        charts.router,
        history.router,
        conversions.router,
        settings.router,
    )
    await start_scheduler(bot)  # Start scheduler for reports and alerts
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
