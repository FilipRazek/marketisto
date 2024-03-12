from api import get_time_series, get_earliest_timestamp
from calc import get_expected_yearly_variation

symbol = "AAPL"


def get_summary(symbol):
    start_date = get_earliest_timestamp(symbol)
    time_series = get_time_series(symbol, start_date)
    yearly_variation = f"{100 * get_expected_yearly_variation(time_series):.2f}%"
    return (
        symbol,
        start_date,
        f"${time_series[0].value}",
        f"${time_series[-1].value}",
        yearly_variation,
    )


print(get_summary(symbol))
