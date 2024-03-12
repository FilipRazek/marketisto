from api import get_time_series, get_earliest_timestamp


def get_daily_variations(time_series):
    variations = []
    for i in range(1, len(time_series)):
        current = time_series[i].value
        previous = time_series[i - 1].value
        variations.append((current - previous) / previous)
    return variations


def get_expected_yearly_variation(time_series):
    daily_variations = get_daily_variations(time_series)
    total_growth = 1
    for variation in daily_variations:
        total_growth *= 1 + variation
    return total_growth ** (365 / len(daily_variations)) - 1


def get_summary(symbol):
    start_date = get_earliest_timestamp(symbol)
    time_series = get_time_series(symbol, start_date)
    yearly_variation = f"{100 * get_expected_yearly_variation(time_series):.2f}%"
    return [
        symbol,
        start_date,
        f"${time_series[0].value}",
        f"${time_series[-1].value}",
        yearly_variation,
    ]
