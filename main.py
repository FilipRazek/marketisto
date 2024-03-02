from api import get_time_series


symbol = "AAPL"


def get_daily_variations(time_series):
    variations = []
    for i in range(1, len(time_series)):
        current = time_series[i].value
        previous = time_series[i - 1].value
        variations.append((current - previous) / previous)
    return variations


def get_expected_daily_variation(symbol):
    time_series = get_time_series(symbol)
    daily_variations = get_daily_variations(time_series)
    total_growth = 1
    for variation in daily_variations:
        total_growth *= 1 + variation
    return total_growth ** (1 / len(daily_variations)) - 1


print(get_expected_daily_variation(symbol))
