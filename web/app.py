from flask import Flask, render_template
from utils.data_fetcher import get_dollar_price, get_gold_prices, get_crypto_prices

app = Flask(__name__)


@app.route("/")
async def index():
    dollar = await get_dollar_price()
    gold = await get_gold_prices()
    cryptos = await get_crypto_prices()
    return render_template("index.html", dollar=dollar, gold=gold, cryptos=cryptos)


if __name__ == "__main__":
    app.run(debug=True)
