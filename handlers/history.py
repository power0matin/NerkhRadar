from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from utils.data_fetcher import get_price_history

router = Router()

@router.message(Command("history"))
async def cmd_history(message: Message):
    try:
        _, asset = message.text.split()
        history = await get_price_history(asset.lower(), "weekly")
        response = f"📜 تاریخچه قیمت {asset.upper()} (7 روز گذشته):\n"
        for date, price in zip(history["dates"], history["prices"]):
            response += f"{date}: {price}\n"
        await message.answer(response)
    except:
        await message.answer("فرمت نادرست! مثال: /history btc")