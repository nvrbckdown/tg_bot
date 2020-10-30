import pyowm
import settings

owm = pyowm.OWM(settings.OWM_URL)


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
