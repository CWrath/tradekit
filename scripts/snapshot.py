import os
import yfinance as yf

with open('sp500_tickers.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start='2021-01-01', end='2021-02-05')
        data.to_csv("datasets/{}.csv".format(symbol))
