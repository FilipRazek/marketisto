from api import get_time_series, get_earliest_timestamp
from calc import get_expected_yearly_variation

symbol = "AAPL"


def get_summary(symbol):
    start_date = get_earliest_timestamp(symbol)
    time_series = get_time_series(symbol, start_date)
    expected_variation = get_expected_yearly_variation(time_series)
    return start_date, expected_variation


print(get_summary(symbol))
