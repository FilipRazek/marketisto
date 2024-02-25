import requests
import matplotlib.pyplot as plt

from date_utils import add_years, is_in_future
from eod import EndOfDay

symbol = "AAPL"
api_key = "demo"

URL_BASE = "https://api.twelvedata.com/"


def build_url(base, endpoint, params):
    url = base + endpoint + "?"
    for key, value in params.items():
        url += key + "=" + value + "&"
    return url


def get_earliest_timestamp(symbol):
    url = build_url(
        URL_BASE,
        "earliest_timestamp",
        {"symbol": symbol, "apikey": api_key, "interval": "1day"},
    )
    response = requests.get(url).json()
    return response["datetime"]


def get_time_series_between_dates(symbol, start_date, end_date):
    params = {
        "symbol": symbol,
        "apikey": api_key,
        "interval": "1day",
        "start_date": start_date,
    }
    if end_date:
        params["end_date"] = end_date
    url = build_url(
        URL_BASE,
        "time_series",
        params,
    )

    response = requests.get(url).json()
    try:
        return [
            EndOfDay(symbol, value["datetime"], value["close"])
            for value in response["values"][::-1]
        ]
    except Exception as e:
        print(symbol, start_date, end_date)
        print(response)
        raise e


def get_time_series(symbol):
    start_date = get_earliest_timestamp(symbol)
    MAX_YEARS = 18
    values = []
    running = True
    while running:
        end_date = add_years(start_date, MAX_YEARS)
        if is_in_future(end_date):
            end_date = None
            running = False
        new_values = get_time_series_between_dates(
            symbol, start_date, end_date)
        values.extend(new_values)
        start_date = end_date
    return values


time_series = get_time_series(symbol)

x = []
y = []
for eod in time_series:
    x.append(eod.date)
    y.append(eod.value)

plt.plot(x, y)
plt.show()
