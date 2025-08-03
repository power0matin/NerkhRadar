import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from database import get_all_users
from utils.data_fetcher import get_dollar_price, get_crypto_price
from utils.pdf_generator import generate_weekly_report

scheduler = AsyncIOScheduler()


async def send_daily_report(bot: Bot):
    users = get_all_users()
    for user in users:
        dollar = await get_dollar_price()
        btc = await get_crypto_price("bitcoin")
        report = f"📊 گزارش روزانه:\nدلار: {dollar} تومان\nبیت‌کوین: ${btc}"
        await bot.send_message(user["id"], report)


async def check_alerts(bot: Bot):
    users = get_all_users()
    for user in users:
        alerts = user.get("alerts", [])
        for alert in alerts:
            current_price = (
                await get_dollar_price()
                if alert["asset"] == "dollar"
                else await get_crypto_price(alert["asset"])
            )
            if (alert["condition"] == ">" and current_price > alert["value"]) or (
                alert["condition"] == "<" and current_price < alert["value"]
            ):
                await bot.send_message(
                    user["id"], f"⚠️ هشدار: {alert['asset']} به {current_price} رسید!"
                )


async def start_scheduler(bot: Bot):
    scheduler.add_job(send_daily_report, "cron", hour=14, minute=0, args=[bot])
    scheduler.add_job(check_alerts, "interval", minutes=5, args=[bot])
    scheduler.start()
