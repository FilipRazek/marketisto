import requests
import redis
from eod import EndOfDay
from utils.date import add_years, is_in_future
from utils.url import build_url

URL_BASE = "https://api.twelvedata.com/"

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def cache_response(endpoint, key, response):
    r.hset(endpoint, key, response)

def get_cached_response(endpoint, key):
    return r.hget(endpoint, key)


def get_earliest_timestamp(symbol, api_key):
    cached = get_cached_response("earliest_timestamp", symbol)
    url = build_url(
        URL_BASE,
        "earliest_timestamp",
        {"symbol": symbol, "apikey": api_key, "interval": "1day"},
    )
    response = requests.get(url).json()
    try:
        result = response["datetime"]
        cache_response("earliest_timestamp", symbol, result)
        return result
    except Exception as e:
        print(symbol)
        print(response)
        raise e


def get_time_series_between_dates(symbol, start_date, end_date, api_key):
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
            EndOfDay(symbol, value["datetime"], float(value["close"]))
            for value in response["values"][::-1]
        ]
    except Exception as e:
        print(symbol, start_date, end_date)
        print(response)
        raise e


def get_time_series(symbol, start_date, api_key):
    MAX_YEARS = 18
    values = []
    running = True
    while running:
        end_date = add_years(start_date, MAX_YEARS)
        if is_in_future(end_date):
            end_date = None
            running = False
        new_values = get_time_series_between_dates(
            symbol, start_date, end_date, api_key)
        values.extend(new_values)
        start_date = end_date
    return values
