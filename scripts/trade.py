import json
import requests

API_KEY = 'PKOU1V1N3TK3NEUTKZA7'
SECRET_KEY = 'TpvOwzcbnh1iP4yLexNI8ey4j4TJ1PQu0wGusE1t'

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, type, side, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

response = create_order("APPL", 100, "buy", "market", "gtc")

print(response)