from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from utils.data_fetcher import get_dollar_price, get_gold_prices, get_crypto_prices, get_crypto_price

router = Router()

@router.message(Command("dollar"))
async def cmd_dollar(message: Message):
    price = await get_dollar_price()
    await message.answer(f"💵 قیمت دلار بازار آزاد: {price} تومان")

@router.message(Command("gold"))
async def cmd_gold(message: Message):
    prices = await get_gold_prices()
    response = (
        f"🪙 قیمت طلا:\n"
        f"هر گرم: {prices['gram']} تومان\n"
        f"سکه: {prices['coin']} تومان\n"
        f"انس جهانی: {prices['ounce']} دلار"
    )
    await message.answer(response)

@router.message(Command("crypto"))
async def cmd_crypto(message: Message):
    prices = await get_crypto_prices()
    response = "💸 قیمت رمزارزها:\n"
    for coin, price in prices.items():
        response += f"{coin.upper()}: ${price}\n"
    await message.answer(response)

@router.message(Command("coin"))
async def cmd_coin(message: Message):
    coin = message.text.split()[1].lower() if len(message.text.split()) > 1 else None
    if coin:
        price = await get_crypto_price(coin)
        await message.answer(f"💰 قیمت {coin.upper()}: ${price}")
    else:
        await message.answer("لطفاً نام رمزارز را مشخص کنید، مثال: /coin btc")