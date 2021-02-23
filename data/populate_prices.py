import sqlite3
from datetime import datetime, date, timedelta
import alpaca_trade_api as tradeapi
import config
import tulipy
import numpy
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

    data = api.polygon.historic_agg_v2(symbol, multiplier='1', timespan='day', _from=startdate, to=enddate).df
    print(f"processing symbol {symbol}")
    print(data)

    cursor.execute("""
        INSERT INTO ohlc_data (dt, symbol, open, high, low, close, volume, vwap)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (enddate, symbols, data.open, data.high, data.low, data.close, data.volume, data.vwap))

    connection.commit()




