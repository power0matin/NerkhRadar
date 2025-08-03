import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


async def get_dollar_price():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.tgju.org/") as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            price = soup.find(
                "div", class_="price"
            ).text.strip()  # Adjust selector as needed
            return float(price.replace(",", ""))


async def get_gold_prices():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.tgju.org/") as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            return {
                "gram": float(
                    soup.find("div", class_="gold-gram").text.replace(",", "")
                ),
                "coin": float(
                    soup.find("div", class_="gold-coin").text.replace(",", "")
                ),
                "ounce": float(
                    soup.find("div", class_="gold-ounce").text.replace(",", "")
                ),
            }


async def get_crypto_prices(coins=["bitcoin", "ethereum", "solana"]):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd"
        async with session.get(url) as response:
            data = await response.json()
            return {coin: data[coin]["usd"] for coin in coins}


async def get_crypto_price(coin):
    prices = await get_crypto_prices([coin])
    return prices.get(coin, 0)


async def get_price_history(asset, period):
    # Mock implementation (replace with real API or DB query)
    dates = [
        (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)
    ]
    prices = [1000 + i * 10 for i in range(7)]  # Placeholder
    return {"dates": dates, "prices": prices}
