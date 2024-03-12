import sys
from util import build_summary_table

symbols = [symbol.upper() for symbol in sys.argv[1:]]
print(build_summary_table(symbols))
