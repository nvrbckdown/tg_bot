import pyowm

owm = pyowm.OWM("daeff41c7c57750a4dedf5fb0d4c3de2")


class Weather:
    """Weather from service"""
    city = ""

    def __init__(self, city="Tashkent"):
        self.city = city

    def __get_weather(self):
        #TODO get weather info from server and return it to user
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(self.city)
        weather_from_service = observation.weather
        weather = [weather_from_service.wind(), weather_from_service.temperature('celsius'), weather_from_service.humidity,
                   weather_from_service.pressure, weather_from_service.detailed_status]
        return weather

    def return_weather(self):
        return self.__get_weather()


if __name__ == "__main__":
    w = Weather()
    weather = w.return_weather()
    print(weather[0])
    print(weather[1]["temp"])
    print(weather)