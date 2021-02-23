import config
import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import date


api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

# all of these examples work
aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from='2019-01-01', to='2019-02-01').df
aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from=date.datetime(2019, 1, 1), to='2019-02-01').df
aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from=date.date(2019, 1, 1), to='2019-02-01').df
aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from=pd.Timestamp('2019-01-01'), to='2019-02-01').df
# timestamp should be in milliseconds datetime.datetime(2019, 1, 1).timestamp()*1000 == 1546293600000
aapl = api.polygon.historic_agg_v2('AAPL', 1, 'day', _from=1546293600000, to='2019-02-01').df

print(aapl)


# # Get a list of all active assets.
# active_assets = api.list_assets(status='active')
#
# # Filter the assets down to just those on NASDAQ.
# nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
# print(nasdaq_assets)

#
# gap = 100 * (todayopenprice - yesterdaycloseprice) / todayopenprice
#
# if gap > 50:
#     True
# else:
#     False

