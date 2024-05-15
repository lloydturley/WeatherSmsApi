#  a class that will hold a forecast with the fields date & time,
#  feels_like, humidity, clouds, wind, rain, and weather_description

class Forecast:
    def __init__(self, date_time, temperature, feels_like, humidity, clouds, wind, rain, weather_description):
        self.date_time = date_time
        self.temperature = temperature
        self.feels_like = feels_like
        self.humidity = humidity
        self.clouds = clouds
        self.wind = wind
        self.rain = rain
        self.weather_description = weather_description
