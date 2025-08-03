# TODO List for Telegram Market Bot

## Completed Tasks

- [x] Implement main bot logic using `aiogram` (`bot.py`)
- [x] Create command handlers for real-time prices (`/dollar`, `/gold`, `/crypto`, `/coin`)
- [x] Set up SQLite database for user settings and alerts (`database.py`)
- [x] Implement daily report scheduling at 14:00 with configurable time (`scheduler.py`, `/settime`)
- [x] Add price alerts for >3% changes and custom thresholds (`alerts.py`, `/alert`)
- [x] Generate price charts using Matplotlib (`charts.py`, `/chart`)
- [x] Display price history for 7 days (`history.py`, `/history`)
- [x] Implement currency conversion (`conversions.py`, `/convert`)
- [x] Add user settings management (`settings.py`, `/settings`, `/setcurrency`, `/setcrypto`)
- [x] Create basic PDF report generator (`pdf_generator.py`)
- [x] Set up Flask web app for price visualization (`web/app.py`)
- [x] Fetch dollar and gold prices via web scraping (mock implementation, `data_fetcher.py`)
- [x] Fetch cryptocurrency prices via CoinGecko API (`data_fetcher.py`)
- [x] Define project structure and dependencies (`requirements.txt`)

## Pending Tasks

- [ ] Implement language switching (Persian/English):
  - Store user language preference in SQLite database.
  - Use translation dictionaries for bot messages and reports.
- [ ] Add news fetching feature:
  - Scrape 2 daily news items from economic sites (e.g., Bloomberg).
  - Format news with title, summary, and link.
  - Schedule news delivery in `scheduler.py`.
- [ ] Enhance PDF reports:
  - Include charts and more detailed data in weekly reports.
  - Add support for Persian text rendering (use appropriate LaTeX font or library).
- [ ] Implement Android app:
  - Develop using Kivy or Flutter to replicate web app functionality.
  - Integrate with the same backend APIs.
- [ ] Improve web scraping reliability:
  - Update `data_fetcher.py` with accurate selectors for `tgju.org`.
  - Add error handling for failed scrapes or site changes.
- [ ] Enhance web app:
  - Add interactive charts using Plotly.js.
  - Implement user authentication and personalized settings.
- [ ] Add price history storage:
  - Store price data in SQLite for accurate `/history` and `/chart` commands.
  - Fetch historical data from APIs where available (e.g., CoinGecko).
- [ ] Optimize alert system:
  - Improve performance of price checks (e.g., batch API calls).
  - Add option to disable alerts (`/disable_alert`).
- [ ] Test and validate:
  - Write unit tests for data fetching and database operations.
  - Test web scraping stability across different network conditions.
- [ ] Deploy the bot:
  - Set up on a cloud service (e.g., Heroku, AWS).
  - Configure webhook for Telegram bot.
- [ ] Document API usage:
  - Add detailed comments in `data_fetcher.py` for API and scraping logic.
  - Update README with API rate limits and scraping considerations.
