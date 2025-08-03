# NerkhRadar 📊

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![aiogram](https://img.shields.io/badge/aiogram-3.8.0-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-green)

**NerkhRadar** (نرخ‌ردار) is a powerful Telegram bot built with Python and `aiogram` to deliver real-time market data for dollar, gold, and cryptocurrencies. With features like price alerts, daily/weekly reports, price history, charts, and currency conversion, NerkhRadar keeps you informed about market trends. It also includes a Flask-based web app for price visualization. Designed for modularity and extensibility, NerkhRadar is your go-to tool for market monitoring.

## 🚀 Features

| Command                                 | Description                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------- |
| `/dollar`                               | Get real-time dollar price in Toman (from [tgju.org](https://www.tgju.org/)).                                   |
| `/gold`                                 | View prices for gram of gold, gold coin, and global ounce.                                                      |
| `/crypto`                               | List prices for popular cryptocurrencies (BTC, ETH, SOL) via [CoinGecko API](https://www.coingecko.com/en/api). |
| `/coin <symbol>`                        | Get the price of a specific cryptocurrency (e.g., `/coin btc`).                                                 |
| `/chart <asset> <daily                  | weekly>`                                                                                                        | Generate and send a price chart using Matplotlib. |
| `/history <asset>`                      | Display price history for the past 7 days.                                                                      |
| `/convert <amount> <asset> to <target>` | Convert between currencies (e.g., `/convert 100 usdt to toman`).                                                |
| `/alert <asset> <condition> <value>`    | Set custom price alerts (e.g., `/alert btc >110000`).                                                           |
| `/settings`                             | Manage user preferences (currency, report time, crypto list).                                                   |
| `/settime HH:MM`                        | Set custom time for daily reports.                                                                              |
| `/setcurrency <toman                    | dollar                                                                                                          | tether>`                                          | Set preferred currency. |
| `/setcrypto <coin1,coin2,...>`          | Customize cryptocurrency watchlist.                                                                             |

### Additional Features

- **Daily Reports**: Automated market updates at 14:00 (configurable via `/settime`).
- **Price Alerts**: Notifies for >3% price changes or custom thresholds, checked every 5 minutes.
- **Weekly PDF Reports**: Summarizes market data in a downloadable PDF.
- **Web App**: Flask-based dashboard for price visualization at `http://localhost:5000`.

## 📂 Project Structure

```plaintext
nerkhradar/
├── bot.py              # Main bot logic for NerkhRadar
├── handlers/           # Command handlers
│   ├── commands.py     # Price commands (/dollar, /gold, /crypto, /coin)
│   ├── alerts.py       # Price alert management
│   ├── charts.py       # Chart generation
│   ├── history.py      # Price history
│   ├── conversions.py  # Currency conversion
│   ├── settings.py     # User settings
├── utils/              # Utility functions
│   ├── data_fetcher.py # Data fetching (APIs, web scraping)
│   ├── pdf_generator.py# PDF report generation
├── scheduler.py        # Scheduling for reports and alerts
├── database.py         # SQLite database management
├── templates/          # HTML templates
│   ├── report_template.html
├── web/                # Flask web app
│   ├── app.py
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
├── TODO.md             # Development tasks
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Git
- Telegram bot token (from [BotFather](https://t.me/BotFather))

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/nerkhradar.git
   cd nerkhradar
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure NerkhRadar**:

   - Replace `YOUR_TELEGRAM_BOT_TOKEN` in `bot.py` with your Telegram bot token.

5. **Run NerkhRadar**:

   ```bash
   python bot.py
   ```

6. **Run the Web App** (optional):
   ```bash
   cd web
   python app.py
   ```
   Access the web app at `http://localhost:5000`.

## 📚 Dependencies

Key dependencies (full list in `requirements.txt`):

- `aiogram==3.8.0`: Telegram bot framework
- `aiohttp==3.9.5`: Asynchronous HTTP requests
- `beautifulsoup4==4.12.3`: Web scraping
- `matplotlib==3.9.1`: Chart generation
- `fpdf==1.7.2`: PDF generation
- `apscheduler==3.10.4`: Task scheduling
- `flask==3.0.3`: Web app framework

## 🌐 Data Sources

- **Dollar & Gold**: Scraped from [tgju.org](https://www.tgju.org/) (update selectors in `data_fetcher.py` as needed).
- **Cryptocurrencies**: Fetched from [CoinGecko API](https://www.coingecko.com/en/api) (free, no authentication required).
- **News**: Planned for future implementation (e.g., scraping Bloomberg).

## ⚙️ Usage

1. **Start NerkhRadar**:

   - Run `python bot.py` to launch the Telegram bot.
   - Interact via commands (e.g., `/dollar`, `/chart btc daily`).

2. **Web App**:

   - Run `python web/app.py` to start the Flask app.
   - View real-time prices in your browser at `http://localhost:5000`.

3. **Database**:
   - User settings and alerts are stored in `bot.db` (SQLite).
   - Automatically initialized on first run.

## 🔍 Notes

<details>
<summary>Important Considerations</summary>

- **Web Scraping**: The `tgju.org` selectors in `data_fetcher.py` are placeholders. Inspect the site’s HTML and update selectors for reliability.
- **Language Support**: Persian is default; English support is planned (see `TODO.md`).
- **Android App**: Not implemented but can be developed using Kivy or Flutter.
- **Rate Limits**: CoinGecko API has rate limits; avoid excessive calls.
- **Error Handling**: Add robust error handling for production use.

</details>

## 🤝 Contributing

Contributions to NerkhRadar are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Check `TODO.md` for open tasks and feature ideas.

## 📜 License

NerkhRadar is licensed under the [MIT License](LICENSE).

## 📬 Contact

For issues or suggestions, open an issue on GitHub or contact [your-email@example.com](mailto:your-email@example.com).

⭐ **Star NerkhRadar on GitHub** if you find it useful!  
🔗 [View on GitHub](https://github.com/your-username/nerkhradar)
