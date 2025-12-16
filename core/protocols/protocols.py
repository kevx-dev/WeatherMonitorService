from typing import Protocol

from core.domains.location import Location
from core.domains.weather import Weather


class WeatherProtocol(Protocol):

    def get_weather(self, location: Location) -> Weather:
        ...
