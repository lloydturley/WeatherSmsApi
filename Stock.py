class Stock:
    def __init__(self, ticker, change, last_close, thirty_day_close, thirty_day_change, ninety_day_close,
                 ninety_day_change):
        self.ticker = ticker
        self.change = change
        self.last_close = last_close
        self.thirty_day_close = thirty_day_close
        self.thirty_day_change = thirty_day_change
        self.ninety_day_close = ninety_day_close
        self.ninety_day_change = ninety_day_change

