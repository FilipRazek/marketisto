class EndOfDay:
    def __init__(self, symbol, date, value):
        self.symbol = symbol
        self.date = date
        self.value = value

    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.value}"
