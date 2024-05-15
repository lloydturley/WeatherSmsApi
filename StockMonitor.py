import requests
import datetime
from Stock import Stock


class StockMonitor:

    def __init__(self, tickers):
        self.tickers = tickers
        print(self.tickers)
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
            # url = '?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
            #response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo")
            response = requests.get("https://www.alphavantage.co/query", params=parameters)
            response.raise_for_status()
            data = response.json()
            print(data)
            print()

            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            yesterday = yesterday.strftime('%Y-%m-%d')
            print(f"yesterday: {yesterday}")
            print()
            day_before = datetime.datetime.now() - datetime.timedelta(days=2)
            day_before = day_before.strftime('%Y-%m-%d')
            thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
            thirty_days_ago = thirty_days_ago.strftime('%Y-%m-%d')
            ninety_days_ago = datetime.datetime.now() - datetime.timedelta(days=90)
            ninety_days_ago = ninety_days_ago.strftime('%Y-%m-%d')

            stock = Stock(
                ticker=ticker,
                change=self.calc_change(
                    last_close=float(data["Time Series (Daily)"][yesterday]["4. close"]),
                    prev_close=float(data["Time Series (Daily)"][day_before]["4. close"]),
                ),
                last_close=data["Time Series (Daily)"][yesterday]["4. close"],
                thirty_day_close=data["Time Series (Daily)"][thirty_days_ago]["4. close"],
                thirty_day_change=self.calc_change(
                    last_close=float(data["Time Series (Daily)"][yesterday]["4. close"]),
                    prev_close=float(data["Time Series (Daily)"][thirty_days_ago]["4. close"]),
                ),
                ninety_day_close=data["Time Series (Daily)"][ninety_days_ago]["4. close"],
                ninety_day_change=self.calc_change(
                    last_close=float(data["Time Series (Daily)"][yesterday]["4. close"]),
                    prev_close=float(data["Time Series (Daily)"][ninety_days_ago]["4. close"]),
                )
            )
            self.stocks.append(stock)

    def calc_change(self, last_close, prev_close):
        return round((last_close - prev_close) / prev_close * 100, 2)