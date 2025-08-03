from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from database import update_user_settings, get_user_settings

router = Router()


@router.message(Command("settings"))
async def cmd_settings(message: Message):
    settings = get_user_settings(message.from_user.id)
    response = (
        f"⚙️ تنظیمات:\n"
        f"واحد پول: {settings.get('currency', 'toman')}\n"
        f"زمان گزارش: {settings.get('report_time', '14:00')}\n"
        f"رمزارزها: {', '.join(settings.get('crypto_list', ['btc', 'eth', 'sol']))}\n"
        "برای تغییر، دستورات زیر را استفاده کنید:\n"
        "/setcurrency toman|dollar|tether\n"
        "/settime HH:MM\n"
        "/setcrypto btc,eth,sol"
    )
    await message.answer(response)


@router.message(Command("settime"))
async def set_time(message: Message):
    try:
        _, time = message.text.split()
        update_user_settings(message.from_user.id, report_time=time)
        await message.answer(f"زمان گزارش به {time} تنظیم شد.")
    except:
        await message.answer("فرمت نادرست! مثال: /settime 14:00")
