import re
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from database import add_alert, get_user_alerts
from utils.data_fetcher import get_dollar_price, get_crypto_price

router = Router()


@router.message(Command("alert"))
async def set_alert(message: Message):
    # Use regex to parse /alert <asset> <condition> <value>
    pattern = r"^/alert\s+(\w+)\s*([<>])\s*(\d+\.?\d*)$"
    match = re.match(pattern, message.text.strip()) 
    

    if match:
        asset, condition, value = match.groups()
        value = float(value)
        add_alert(message.from_user.id, asset.lower(), condition, value)
        await message.answer(f"هشدار برای {asset} {condition} {value} تنظیم شد.")
    else:
        await message.answer(
            "فرمت نادرست! مثال: /alert btc >110000 یا /alert dollar <85000"
        )
