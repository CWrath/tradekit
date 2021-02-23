from config import DB_FILE
import sqlite3

connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()

# Creates Table Called 'assets'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id SERIAL PRIMARY KEY,
        class TEXT NOT NULL,
        exchange TEXT NOT NULL,
        symbol TEXT NOT NULL UNIQUE, 
        status TEXT NOT NULL,
        marginable BOOLEAN NOT NULL,
        shortable BOOLEAN NOT NULL
        );
""")

# Creates Table Called 'ohlc_data'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ohlc_data (
        stock_id SERIAL PRIMARY KEY,
        dt TIMESTAMP NOT NULL,
        symbol TEXT NOT NULL,
        open NUMERIC NOT NULL,
        high NUMERIC NOT NULL,
        low NUMERIC NOT NULL,
        close NUMERIC NOT NULL,
        volume NUMERIC NOT NULL,
        CONSTRAINT fk_stock FOREIGN KEY(stock_id) REFERENCES stock(id)
    );
""")

# # Creates Table Called 'stock_price_minute'
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS stock_price_minute (
#         id INTEGER PRIMARY KEY,
#         stock_id INTEGER,
#         datetime NOT NULL,
#         open NOT NULL,
#         high NOT NULL,
#         low NOT NULL,
#         close NOT NULL,
#         volume NOT NULL,
#         FOREIGN KEY (stock_id) REFERENCES stock (id)
#     )
# """)

# Creates Table Called 'tick_data'
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS tick_data (
#         id SERIAL PRIMARY KEY,
#         dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
#         stock_id INTEGER NOT NULL,
#         bid NUMERIC NOT NULL,
#         ask NUMERIC NOT NULL,
#         bid_vol NUMERIC,
#         ask_vol NUMERIC,
#         CONSTRAINT fk_stock FOREIGN KEY(stock_id) REFERENCES stock(id)
#     );
# """)

# # Creates Table Called 'strategy'
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS strategy (
#     id INTEGER PRIMARY KEY,
#     name NOT NULL
#     )
# """)
#
# # Creates Table Called 'stock_strategy'
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS stock_strategy (
#     stock_id INTEGER NOT NULL,
#     strategy_id INTEGER NOT NULL,
#     FOREIGN KEY (stock_id) REFERENCES stock (id)
#     FOREIGN KEY (strategy_id) REFERENCES strategy (id)
#     )
# """)
#
# # Adds Strategy Names to Database
# strategies = ['opening_range_breakout', 'opening_range_breakdown', 'bollinger_bands']
#
# for strategy in strategies:
#     cursor.execute("""
#     INSERT INTO strategy (name) VALUES (?)
#     """, (strategy,))

connection.commit()
