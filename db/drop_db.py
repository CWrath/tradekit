from config import DB_FILE
import sqlite3

connection = sqlite3.connect(DB_FILE)

cursor = connection.cursor()

# DELETE TABLE 'stock'
cursor.execute("""
    DROP TABLE stock
""")

# DELETE TABLE 'ohlc_data'
cursor.execute("""
    DROP TABLE ohlc_data
""")

# # DELETE TABLE 'stock_strategy'
# cursor.execute("""
#     DROP TABLE stock_strategy
# """)
#
# # DELETE TABLE 'strategy'
# cursor.execute("""
#     DROP TABLE strategy
# """)

connection.commit()
