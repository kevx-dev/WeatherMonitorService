from datetime import datetime
from time import sleep

import requests  # type: ignore[import-untyped]

from core.domains.location import Location
from core.domains.weather import Weather
from core.protocols.protocols import WeatherProtocol
import logging

logger = logging.getLogger(__name__)

class WeatherApiClient(WeatherProtocol):

    def get_weather(self, location: Location) -> Weather:

        MAX_ATTEMPT:int = 3
        WAIT_TIME:float = 5

        logger.info(f"Fetching weather for {location}")

        BASE_URL = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": ["temperature_2m", "precipitation_probability"],
            "timezone": "Europe/Berlin",
            "forecast_days": 1,
        }

        for attempt in range(MAX_ATTEMPT):
            try:
                response = requests.get(url=BASE_URL, params=params, timeout=5)
                data: dict[str, dict[str, list]] = response.json()
                logger.info(f"Weather fetched successfully")

                current_hour: int = datetime.now().hour
                hourly: dict[str, list] = data["hourly"]

                actual_weather_time: list[str] = [time for time in hourly["time"] if int(time.split("T")[1].split(":")[0]) == int(current_hour)]
                time_index: int = hourly["time"].index(actual_weather_time[0])

                temp: float = hourly["temperature_2m"][time_index]
                rain: int = hourly["precipitation_probability"][time_index]

                return Weather(
                    location=location.name,
                    temperature_celsius=temp,
                    rain_chance=rain
                )
            except requests.exceptions.RequestException:
                if attempt == 2:
                    logger.error("Failed to fetch weather",exc_info=True)
                    raise
                logger.warning(f"Attempt {attempt + 1} failed. Retrying in {WAIT_TIME} seconds...")
                sleep(WAIT_TIME)
        raise RuntimeError("Unreachable: Weather could not be fetched.")


