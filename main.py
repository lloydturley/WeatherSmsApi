import os
from StockMonitor import StockMonitor
from Weather import Weather
from NewsMonitor import NewsMonitor
from Email import Email

appid = os.environ['OPEN_WEATHER_APP_ID']
lat = os.environ['LAT']
long = os.environ['LON']
news_apikey = os.environ['NEWSAPI_ORG']
email = Email()

weather = Weather(appid, lat, long)
weather.initialize_forecasts()

stcks = os.environ['STOCKS'].split(',')
print(stcks)
stock_monitor = StockMonitor(stcks)
stock_monitor.initialize_stocks(os.environ['ALPHAVANTAGE'])

for item in stock_monitor.stocks:
    if item.change > 5 or item.change < -5:
        email.add_to_body(f"{item.ticker} has BIG swing {item.change}%")
    else:
        email.add_to_body(f"{item.ticker} has small swing {item.change}%")
    email.add_to_body(f"Last close: {item.last_close}")
    email.add_to_body(f"30 day change: {item.thirty_day_change}%")
    email.add_to_body(f"30 day close: {item.thirty_day_close}")
    email.add_to_body(f"90 day change: {item.ninety_day_change}%")
    email.add_to_body(f"90 day close: {item.ninety_day_close}")
    email.add_to_body("\n")

news_monitor = NewsMonitor()
news_monitor.initialize_articles(news_apikey)
for article in news_monitor.articles:
    email.add_to_body(article.title)
    email.add_to_body(article.description)
    email.add_to_body(article.url)
    email.add_to_body("\n")


for forecast in weather.forecasts:
    email.add_to_body(forecast.date_time)
    email.add_to_body(f"Temperature: {forecast.temperature}°F")
    email.add_to_body(f"Feels like: {forecast.feels_like}°F")
    email.add_to_body(f"Humidity: {forecast.humidity}%")
    email.add_to_body(f"Clouds: {forecast.clouds}%")
    email.add_to_body(f"Wind: {forecast.wind} mph")
    email.add_to_body(f"Rain: {forecast.rain} in")
    email.add_to_body(f"Weather: {forecast.weather_description}")
    email.add_to_body("\n")

print(email.body)

email.send_email(os.environ['SEND_EMAIL_LOGIN'], os.environ['SEND_EMAIL_PASSWORD'], "Daily Brief")

# send
# ticker, % change, up or down, articles title & description x3
