import os
import pandas
import plotly.graph_objects as go

symbols = []

for filename in os.listdir('datasets'):
    symbol = filename.split(".")[0]
    df = pandas.read_csv('datasets/{}'.format(filename))
    if df.empty:
        continue

    df['20sma'] = df['Close'].rolling(window=20).mean()
    df['stddev'] = df['Close'].rolling(window=20).std()
    df['lower_band'] = df['20sma'] - (2 * df['stddev'])
    df['upper_band'] = df['20sma'] + (2 * df['stddev'])

    df['TR'] = abs(df['High'] - df['Low'])
    df['ATR'] = df['TR'].rolling(window=20).mean()

    df['upperKC'] = df['20sma'] + (df['ATR'] * 1.5)
    df['lowerKC'] = df['20sma'] - (df['ATR'] * 1.5)

    def in_squeeze(df):
        return df['lower_band'] > df['lowerKC'] and df['upper_band'] < df['upperKC']

    df['squeeze_on'] = df.apply(in_squeeze, axis=1)

    if df.iloc[-2]['squeeze_on'] and not df.iloc[-1]['squeeze_on']:
        print("{} coming out of the squeeze".format(symbol))

    if symbol in symbols:
        print(df)

candlestick = go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
upper_band = go.Scatter(x=df['Date'], y=df['upper_band'], name='Upper Bollinger Band', line={'color': 'red'})
lower_band = go.Scatter(x=df['Date'], y=df['lower_band'], name='Lower Bollinger Band', line={'color': 'red'})
upperKC = go.Scatter(x=df['Date'], y=df['upperKC'], name='Upper Kelter Channel', line={'color': 'blue'})
lowerKC = go.Scatter(x=df['Date'], y=df['lowerKC'], name='Lower Kelter Channel', line={'color': 'blue'})

fig = go.Figure(data=[candlestick, upper_band, lower_band])
fig.layout.xaxis.type = 'category'
fig.layout.xaxis.rangeslider.visible = False


fig.show()
