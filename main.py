import os
from StockMonitor import StockMonitor
from Weather import Weather
from NewsMonitor import NewsMonitor
from Email import Email
from airBrentals import airBrentals

appid = os.environ['OPEN_WEATHER_APP_ID']
MY_LAT = os.environ['NOTIFY_LAT']
MY_LON = os.environ['NOTIFY_LON']
news_apikey = os.environ['NEWSAPI_ORG']
LOCATION_TO_QUERY = os.environ['NOTIFY_RENTAL_LOC']
AIRBNB_API_KEY = os.environ['NOTIFY_APIFY']

email = Email()

weather = Weather(appid, MY_LAT, MY_LON)
weather.initialize_forecasts()

stcks = os.environ['STOCKS'].split(',')
stock_monitor = StockMonitor(stcks)
stock_monitor.initialize_stocks(os.environ['ALPHAVANTAGE'])

email.add_to_body("STOCKS:")
for item in stock_monitor.stocks:
    if item.change > 5 or item.change < -5:
        email.add_to_body(f"{item.ticker} has a BIG swing {item.change}%")
    else:
        email.add_to_body(f"{item.ticker} has a small swing {item.change}%")
    email.add_to_body(f"Last close: {item.last_close}")
    email.add_to_body(f"30 day change: {item.thirty_day_change}%")
    email.add_to_body(f"30 day close: {item.thirty_day_close}")
    email.add_to_body(f"90 day change: {item.ninety_day_change}%")
    email.add_to_body(f"90 day close: {item.ninety_day_close}")
    email.add_to_body()

email.add_to_body("NEWS:")
news_monitor = NewsMonitor()
news_monitor.initialize_articles(news_apikey)
for article in news_monitor.articles:
    email.add_to_body(article.title)
    email.add_to_body(article.description)
    email.add_to_body(article.url)
    email.add_to_body()

email.add_to_body("WEATHER:")
for forecast in weather.forecasts:
    email.add_to_body(forecast.date_time)
    email.add_to_body(f"Temperature: {forecast.temperature}F")
    email.add_to_body(f"Feels like: {forecast.feels_like}F")
    email.add_to_body(f"Humidity: {forecast.humidity}%")
    email.add_to_body(f"Clouds: {forecast.clouds}%")
    email.add_to_body(f"Wind: {forecast.wind} mph")
    email.add_to_body(f"Rain: {forecast.rain} in")
    email.add_to_body(f"Weather: {forecast.weather_description}")
    email.add_to_body()

airbnb = airBrentals(MY_LAT, MY_LON, AIRBNB_API_KEY)
rentalResults = airbnb.get_local_listings(LOCATION_TO_QUERY)

email.add_to_body("RENTALS:")
for rental in rentalResults:
    email.add_to_body(f"Name: {rental.name}")
    email.add_to_body(f"Location: {rental.address}")
    email.add_to_body(f"URL: {rental.url}")
    email.add_to_body()


email.add_to_body("End of Brief")

email.send_email(os.environ['SEND_EMAIL_LOGIN'], os.environ['SEND_EMAIL_PASSWORD'], "Daily Brief",
                 os.environ['RECEIVE_EMAIL'])