import requests

symbol = "AAPL"
api_key = "demo"

URL_BASE = "https://api.twelvedata.com/"

def build_url(base, endpoint, params):
    url = base + endpoint + "?"
    for key, value in params.items():
        url += key + "=" + value + "&"
    return url

def get_earliest_timestamp(symbol):
    url = build_url(URL_BASE, "earliest_timestamp", {"symbol": symbol, "apikey": api_key, "interval": "1day"})
    response = requests.get(url).json()
    return response["datetime"]

print(get_earliest_timestamp(symbol))
