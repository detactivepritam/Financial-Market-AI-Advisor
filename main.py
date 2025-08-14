import nest_asyncio
nest_asyncio.apply()
import asyncio
import pandas as pd
import numpy as np
import streamlit as st
from alpaca.data.live import StockDataStream

ALPACA_API_KEY = "Your api key" 
ALPACA_API_SECRET = "Your api secret"

def get_alpaca_stream(symbol, on_price):
	stream = StockDataStream(ALPACA_API_KEY, ALPACA_API_SECRET)
	async def handle_trade(data):
		price = data.price
		timestamp = pd.Timestamp(data.timestamp)
		await on_price({'symbol': symbol, 'price': price, 'timestamp': timestamp})
	stream.subscribe_trades(handle_trade, symbol)
	return stream

async def price_feed(symbol):
	queue = asyncio.Queue()
	async def on_price(data):
		await queue.put(data)
	stream = get_alpaca_stream(symbol, on_price)
	task = asyncio.create_task(stream.run())
	while True:
		data = await queue.get()
		yield data

def calculate_sma(prices, window=10):
	return prices.rolling(window=window).mean()

def calculate_ema(prices, window=10):
	return prices.ewm(span=window, adjust=False).mean()

def calculate_rsi(prices, window=14):
	delta = prices.diff()
	gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
	loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
	rs = gain / loss
	rsi = 100 - (100 / (1 + rs))
	return rsi

def generate_signal(prices):
	sma_short = calculate_sma(prices, window=5)
	sma_long = calculate_sma(prices, window=20)
	rsi = calculate_rsi(prices, window=14)
	if len(prices) < 20:
		return 'Hold'
	if sma_short.iloc[-1] > sma_long.iloc[-1] and rsi.iloc[-1] < 70:
		return 'Buy'
	elif sma_short.iloc[-1] < sma_long.iloc[-1] and rsi.iloc[-1] > 30:
		return 'Sell'
	else:
		return 'Hold'

def run_dashboard():
	st.title('Financial Market AI Advisor')
	symbol = st.text_input('Stock Symbol', 'AAPL')
	st.write('Receiving live prices for:', symbol)
	prices = []
	timestamps = []
	signal = 'Hold'
	placeholder = st.empty()
	async def stream():
		async for data in price_feed(symbol):
			prices.append(data['price'])
			timestamps.append(data['timestamp'])
			df = pd.DataFrame({'price': prices}, index=timestamps)
			if len(df) >= 20:
				signal = generate_signal(df['price'])
				df['SMA_5'] = calculate_sma(df['price'], window=5)
				df['SMA_20'] = calculate_sma(df['price'], window=20)
				df['RSI_14'] = calculate_rsi(df['price'], window=14)
			with placeholder.container():
				st.line_chart(df['price'])
				if len(df) >= 20:
					st.line_chart(df[['SMA_5', 'SMA_20']])
					st.line_chart(df['RSI_14'])
				st.write(f'Latest Signal: **{signal}**')
			await asyncio.sleep(0.1)
	asyncio.get_event_loop().run_until_complete(stream())

if __name__ == '__main__':
	run_dashboard()