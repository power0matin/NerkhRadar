from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from utils.data_fetcher import get_price_history
import matplotlib.pyplot as plt
import io

router = Router()

@router.message(Command("chart"))
async def cmd_chart(message: Message):
    try:
        _, asset, period = message.text.split()
        if period not in ["daily", "weekly"]:
            raise ValueError
        history = await get_price_history(asset.lower(), period)
        
        plt.figure(figsize=(10, 5))
        plt.plot(history["dates"], history["prices"])
        plt.title(f"Price Chart for {asset.upper()} ({period})")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        plt.close()
        
        photo = FSInputFile(buffer, filename=f"{asset}_chart.png")
        await message.answer_photo(photo)
    except:
        await message.answer("فرمت نادرست! مثال: /chart btc daily")