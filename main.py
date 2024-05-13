import requests

parameters = {
    "appid": "d66a5de821dbf9153c40a062b1c9f700",
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
        print("Bring an umbrella")
        break
