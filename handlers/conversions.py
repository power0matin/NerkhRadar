from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from utils.data_fetcher import get_dollar_price, get_gold_prices, get_crypto_price

router = Router()

@router.message(Command("convert"))
async def cmd_convert(message: Message):
    try:
        _, amount, asset, _, target = message.text.lower().split()
        amount = float(amount)
        if asset == "usdt" and target == "toman":
            dollar_price = await get_dollar_price()
            result = amount * dollar_price
            await message.answer(f"{amount} USDT = {result} تومان")
        elif asset == "gram" and target == "dollar":
            gold_prices = await get_gold_prices()
            result = amount * gold_prices["gram"] / await get_dollar_price()
            await message.answer(f"{amount} گرم طلا = {result} دلار")
        else:
            await message.answer("تبدیل پشتیبانی نمی‌شود!")
    except:
        await message.answer("فرمت نادرست! مثال: /convert 100 usdt to toman")