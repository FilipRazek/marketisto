import sys
from utils.summary import build_summary_table

api_key = sys.argv[1]
symbols = [symbol.upper() for symbol in sys.argv[2:]]
print(build_summary_table(symbols, api_key))
