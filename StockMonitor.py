import requests
import datetime
from Stock import Stock


class StockMonitor:

    def __init__(self, tickers):
        self.tickers = tickers
        self.stocks = []


    def initialize_stocks(self, stockApiKey):
        for ticker in self.tickers:
            parameters = {
                "function": "TIME_SERIES_DAILY",
                "symbol": ticker,
                "outputsize": "compact",
                "datatype": "json",
                "apikey": stockApiKey,
            }
            #response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo")
            response = requests.get("https://www.alphavantage.co/query", params=parameters)
            response.raise_for_status()
            data = response.json()
            closings = list(data["Time Series (Daily)"].values())

            stock = Stock(
                ticker=ticker,
                change=self.calc_change(
                    last_close=float(closings[0]["4. close"]),
                    prev_close=float(closings[1]["4. close"]),
                ),
                last_close=float(closings[0]["4. close"]),
                thirty_day_close=float(closings[29]["4. close"]),
                thirty_day_change=self.calc_change(
                    last_close=float(closings[0]["4. close"]),
                    prev_close=float(closings[29]["4. close"])
                ),
                ninety_day_close=float(closings[89]["4. close"]),
                ninety_day_change=self.calc_change(
                    last_close=float(closings[0]["4. close"]),
                    prev_close=float(closings[89]["4. close"])
                )
            )
            self.stocks.append(stock)

    def calc_change(self, last_close, prev_close):
        return round((last_close - prev_close) / prev_close * 100, 2)