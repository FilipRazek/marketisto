from prettytable import PrettyTable
from api import get_time_series, get_earliest_timestamp
from calc import get_expected_yearly_variation

symbol = "AAPL"


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


def build_summary_table(symbols):
    table = PrettyTable()
    table.field_names = [
        "Symbol",
        "Start Date",
        "Start Price",
        "End Price",
        "Yearly Variation",
    ]
    table.add_rows([get_summary(symbol) for symbol in symbols])
    return table


print(build_summary_table([symbol, symbol, symbol]))
