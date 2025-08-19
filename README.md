
# 📈 Financial Market AI Advisor

An interactive, real-time financial market advisor web app powered by Streamlit and Alpaca's live stock data API. Visualize live prices, technical indicators, and receive AI-generated trading signals for your favorite stocks.

---

## 🚀 Features

- **Live Stock Price Streaming**: Real-time data via Alpaca API
- **Technical Indicators**: SMA, EMA, RSI
- **AI Trading Signals**: Buy, Sell, Hold recommendations
- **Modern Dashboard**: Interactive charts and signal display

---

## 🛠️ Requirements

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Alpaca-py
- nest_asyncio

Install all dependencies easily:
```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/detactivepritam/Financial-Market-AI-Advisor.git
   cd Financial-Market-AI-Advisor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Alpaca API credentials**
   Open `main.py` and replace:
   ```python
   ALPACA_API_KEY = "Your api key"
   ALPACA_API_SECRET = "Your api secret"
   ```

4. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 🖥️ Usage

1. Enter a stock symbol (e.g., `AAPL`) in the dashboard.
2. View live price chart, SMA/EMA/RSI indicators, and the latest AI trading signal.
3. Use the dashboard to monitor and analyze market trends in real time.

---

## 📊 Example Dashboard

![Dashboard Screenshot](https://user-images.githubusercontent.com/your-screenshot.png)

---

## 📚 Documentation

### Main Components

- **main.py**: Core application logic and Streamlit dashboard
- **requirements.txt**: List of required Python packages
- **LICENSE**: MIT License

### Technical Indicators

- **SMA (Simple Moving Average)**: Smooths price data to identify trends
- **EMA (Exponential Moving Average)**: Reacts more quickly to price changes
- **RSI (Relative Strength Index)**: Measures momentum and identifies overbought/oversold conditions

### AI Signal Generation

Signals are generated based on the relationship between short/long SMAs and RSI values:

- **Buy**: Short SMA > Long SMA and RSI < 70
- **Sell**: Short SMA < Long SMA and RSI > 30
- **Hold**: Otherwise

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
