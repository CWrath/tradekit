import config
import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)

assets = api.list_assets(status=None, asset_class=None)

for asset in assets:
    try:
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (id, symbol, name, exchange, shortable) VALUES (?, ?, ?, ?, ?)",
                           (asset.id, asset.symbol, asset.name, asset.exchange, asset.shortable))
    except Exception as e:
        print(asset.symbol)
        print(e)

connection.commit()
