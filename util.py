from api import get_time_series, get_earliest_timestamp
from prettytable import PrettyTable


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


def get_summary(symbol, api_key):
    start_date = get_earliest_timestamp(symbol, api_key)
    time_series = get_time_series(symbol, start_date, api_key)
    yearly_variation = f"{100 * get_expected_yearly_variation(time_series):.2f}%"
    return [
        symbol,
        start_date,
        f"${time_series[0].value}",
        f"${time_series[-1].value}",
        yearly_variation,
    ]


def build_summary_table(symbols, api_key):
    table = PrettyTable()
    table.field_names = [
        "Symbol",
        "Start Date",
        "Start Price",
        "End Price",
        "Yearly Variation",
    ]
    table.add_rows([get_summary(symbol, api_key) for symbol in symbols])
    return table
