import requests
from Forecast import Forecast
from datetime import datetime


# from twilio.rest import Client

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)
class Weather:
    def __init__(self, appid, lat, lon):
        self.appid = appid
        self.lat = lat
        self.lon = lon
        self.forecasts = []

    def initialize_forecasts(self):
        parameters = {
            "appid": self.appid,
            "lat": self.lat,
            "lon": self.lon,
            "units": "imperial",
            "cnt": 5,
        }

        response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        response.raise_for_status()
        received_forecasts = response.json()["list"]

        for forecast_interval in received_forecasts:
            forecast_instance = Forecast(
                date_time=datetime.fromtimestamp(forecast_interval["dt"]).strftime('%Y-%m-%d %H:%M:%S'),
                temperature=int(forecast_interval["main"]["temp"]),
                feels_like=int(forecast_interval["main"]["feels_like"]),
                humidity=forecast_interval["main"]["humidity"],
                clouds=forecast_interval["clouds"]["all"],
                wind=int(forecast_interval["wind"]["speed"]),
                rain=round(forecast_interval["rain"]["3h"] * 0.0393701,1) if "rain" in forecast_interval else 0,
                weather_description=forecast_interval["weather"][0]["description"]
            )
            self.forecasts.append(forecast_instance)

        #if int(fore["weather"][0]["id"]) < 701:
        #pass
        # print(fore["weather"]["description"])
        # message = client.messages \
        #     .create(
        #     body="You will need an umbrella since it is going to rain.",
        #     from_='+18336586059',
        #     to='+16782334569'
        # )
        # print("It is going to rain")
        # print(message.status)
        # break

# print(forecast_narrative)
# message = client.messages \
#     .create(
#     body="You will need an umbrella since it is going to rain.",
#     from_='+18336586059',
#     to='+16782334569'
# )
# print(message.status)
