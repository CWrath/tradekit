# Polygon/Alpaca to provide market data
# Need live data feed for new tick data
# Need historic data for indicators and backtesting

# Everday until today, then everyday at the end of the day (4:30), download the day into the database.

# Filter with these Paramaters
# Pre-Market
# Daily Gap % > 20
# Price 1.50 - 20

# Filter Selects 3-4 stocks each stock will get the buy order below.

# Send Buy Bracket Order (Based on 5M)
# 2:1 profit loss ratio
# IF Profit is 2:1 > SELL 1/2 shares
# Adj Stop loss to breakeven
# IF Profit is 2:1 > SELL remaining shares

# End of Day
# Close all trades at the end of the day.