import datetime
import sqlite3
from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main(from_, to, ticker, timespan):

    key = 'Wkop2OVwv6zvM63pGEJS0muaRPpUODm8'

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        from_ = "2019-01-31"
        to = "2019-02-01"
        ticker = "AAPL"
        timespan = "day"

        resp = client.stocks_equities_aggregates(ticker, 1, timespan, from_, to, unadjusted=False)

        print(f"Day aggregates for {resp.ticker} between {from_} and {to}.")

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")


if __name__ == '__main__':
    # Get Daily Minute Bars for
    main(from_ ="2019-01-31", to="2019-02-01", ticker='AAPL', timespan="day")
