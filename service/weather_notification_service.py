from core.domains.location import Location
from core.protocols.protocols import MessengerProtocol
from service.weather_service import WeatherService


class WeatherNotificationService:

    def __init__(self, messenger: MessengerProtocol, weather_service: WeatherService):
        self.messenger: MessengerProtocol = messenger
        self.weather_service: WeatherService = weather_service

    def run(self, location: Location):
        summary = self.weather_service.get_weather_summary(location=location)
        self.messenger.send_message(summary)
