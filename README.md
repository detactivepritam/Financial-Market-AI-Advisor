# Financial Market AI Advisor

This project is a real-time financial market advisor web app built with Streamlit and Alpaca's live stock data API. It provides live price feeds, technical indicators, and AI-generated trading signals for stocks.

## Features

- Live stock price streaming using Alpaca API
- Calculates technical indicators: SMA, EMA, RSI
- Generates buy/sell/hold signals based on indicator values
- Interactive dashboard with charts and latest trading signal

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Alpaca-py
- nest_asyncio

## Setup

1. Install dependencies:
   ```
   pip install streamlit pandas numpy alpaca-py nest_asyncio
   ```

2. Set your Alpaca API credentials in `main.py`:
   ```python
   ALPACA_API_KEY = "Your api key"
   ALPACA_API_SECRET = "Your api secret"
   ```

3. Run the app:
   ```
   streamlit run main.py
   ```

## Usage

- Enter a stock symbol (e.g., AAPL) in the dashboard.
- View live price chart, SMA/EMA/RSI indicators, and the latest AI trading signal.

## License

MIT
