from aiogram import Router, F
from aiogram.filters import Command, RegexpCommandsFilter
from aiogram.types import Message
from database import add_alert, get_user_alerts
from utils.data_fetcher import get_dollar_price, get_crypto_price

router = Router()

@router.message(RegexpCommandsFilter(regexp_commands=['alert (.*)']))
async def set_alert(message: Message):
    try:
        _, asset, condition, value = message.text.split()
        value = float(value)
        add_alert(message.from_user.id, asset.lower(), condition, value)
        await message.answer(f"هشدار برای {asset} {condition} {value} تنظیم شد.")
    except ValueError:
        await message.answer("فرمت نادرست! مثال: /alert btc >110000 یا /alert dollar <85000")