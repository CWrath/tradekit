from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
from datetime import date
import config

app = FastAPI()

app.mount("/static", StaticFiles(directory="/app/web/static"), name="static")

templates = Jinja2Templates(directory="/app/web/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tradingview_widget")
async def tradingview_widget(request: Request):
    return templates.TemplateResponse("tradingview_widget.html", {"request": request})


@app.get("/allstocks")
async def allstocks(request: Request):
    stock_filter = request.query_params.get('filter', False)
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    current_date = date.today().isoformat()
    #
    # if stock_filter == 'new_closing_highs':
    #     cursor.execute("""
    #     SELECT * FROM (
    #         SELECT symbol, name, stock_id, max(close), date
    #         FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #         group by stock_id
    #         order by symbol
    #     ) where date = (select max(date) from ohlc_data)
    #     """)
    # elif stock_filter == 'new_closing_lows':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, min(close), date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             GROUP by stock_id
    #             ORDER by symbol
    #         ) where date = (select max(date) from ohlc_data)
    #         """)
    # elif stock_filter == 'rsi_overbought':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE rsi_14 > 70
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'rsi_oversold':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE rsi_14 < 30
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'above_sma_20':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE close > sma_20
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'below_sma_20':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE close < sma_20
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'above_sma_50':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE close > sma_50
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'below_sma_50':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE close < sma_50
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # elif stock_filter == 'high_of_day_momo':
    #     cursor.execute("""
    #         SELECT * FROM (
    #             SELECT symbol, name, stock_id, date
    #             FROM ohlc_data JOIN stock on stock.id = ohlc_data.stock_id
    #             WHERE volume > '10000'
    #             AND date = (select max(date) from ohlc_data)
    #         )   ORDER by symbol
    #         """)
    # else:
    #     cursor.execute("""
    #         SELECT id, symbol, name FROM stock ORDER BY symbol
    #         """)

    rows = cursor.fetchall()

    cursor.execute("""
        SELECT symbol, rsi_14, sma_20, sma_50, close, volume
        FROM stock JOIN ohlc_data on ohlc_data.stock_id = stock.id
        WHERE date = (select max(date) from ohlc_data)
    """)

    indicator_rows = cursor.fetchall()
    indicator_values = {}

    for row in indicator_rows:
        indicator_values[row['symbol']] = row

    return templates.TemplateResponse("allstocks.html", {"request": request, "stocks": rows,
                                                         "indicator_values": indicator_values})
