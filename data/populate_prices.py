import sqlite3
from datetime import datetime, timedelta
import alpaca_trade_api as tradeapi
import config
import pandas as pd

# API Connect
api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

# Date Variables
NY = 'America/New_York'
fmt = '%Y-%m-d%'
yesterday = datetime.today() - timedelta(days=1)
today = datetime.today()

startdate = pd.Timestamp(yesterday, tz=NY).isoformat()
enddate = pd.Timestamp(today, tz=NY).isoformat()

# Connect to SQL Db
connection = sqlite3.connect(config.DB_FILE)

connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute("""
    SELECT id, symbol, name FROM stock
    """)
rows = cursor.fetchall()
symbols = []
stock_dict = {}

for row in rows:
    symbol = row['symbol']
    symbols.append(symbol)
    stock_dict[symbol] = row['id']

chunk_size = 200
for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i + chunk_size]

    data = api.polygon.historic_agg_v2(symbol_chunk, multiplier='1', timespan='day', _from=startdate, to=enddate)

    for symbol in data:
        print(f"processing symbol {symbol}")

        for bar in data[symbol]:
            stock_id = stock_dict[symbol]

            cursor.execute("""
                        INSERT INTO ohlc_data (stock_id, dt, symbol, open, high, low, close, volume)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (stock_id, enddate, symbol, bar.o, bar.h, bar.l, bar.c, bar.v))

connection.commit()




