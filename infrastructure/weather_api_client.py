from datetime import datetime

import requests  # type: ignore[import-untyped]
from core.domains.location import Location
from core.domains.weather import Weather
from core.protocols.protocols import WeatherProtocol


class WeatherApiClient(WeatherProtocol):

    def get_weather(self, location: Location) -> Weather:
        BASE_URL = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": ["temperature_2m", "precipitation_probability"],
            "timezone": "Europe/Berlin",
            "forecast_days": 1,
        }

        response = requests.get(url=BASE_URL, params=params)
        response.raise_for_status()
        data: dict[str,dict[str,list]] = response.json()

        current_hour: int = datetime.now().hour
        hourly: dict[str,list] = data["hourly"]

        actual_weather_time: list[str] = [time for time in hourly["time"] if int(time.split("T")[1].split(":")[0]) == int(current_hour)]
        time_index: int = hourly["time"].index(actual_weather_time[0])

        temp: float = hourly["temperature_2m"][time_index]
        rain: int = hourly["precipitation_probability"][time_index]

        return Weather(
            location=location.name,
            temperature_celsius=temp,
            rain_chance=rain
        )
