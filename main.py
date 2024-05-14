import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

parameters = {
    "appid": os.environ['OPEN_WEATHER_APP_ID'],
    #"lat": 35.121929,
    #"lon": -85.344170,
    "lat": 33.340179,
    "lon": -86.630157,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
forecast = response.json()["list"]

for fore in forecast:
    if int(fore["weather"][0]["id"]) < 701:
        # print(fore["weather"]["description"])
        message = client.messages \
            .create(
            body="You will need an umbrella since it is going to rain.",
            from_='+18336586059',
            to='+16782334569'
        )
        print("It is going to rain")
        print(message.status)
        break

message = client.messages \
    .create(
    body="You will need an umbrella since it is going to rain.",
    from_='+18336586059',
    to='+16782334569'
)
print(message.status)
