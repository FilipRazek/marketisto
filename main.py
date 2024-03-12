import sys
from prettytable import PrettyTable

from util import get_summary

symbols = [symbol.upper() for symbol in sys.argv[1:]]


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


print(build_summary_table(symbols))
