from datetime import datetime
from unittest.mock import Mock, patch

from core.domains.location import Location
from core.domains.weather import Weather
from infrastructure.weather_api_client import WeatherApiClient


def test_get_weather_returns_correct_weather_object():
    fake_now = datetime(2025, 12, 16, 14, 0)

    fake_json = {
        "hourly": {
            "time": [
                "2025-12-16T12:00",
                "2025-12-16T13:00",
                "2025-12-16T14:00"
            ],
            "temperature_2m": [5.1, 6.3, 7.2],
            "precipitation_probability": [10, 20, 90]
        }
    }

    fake_response = Mock()
    fake_response.json.return_value = fake_json
    fake_response.raise_for_status.return_value = None

    client = WeatherApiClient()
    location = Location(name="Berlin", latitude=52.52, longitude=13.41)

    with patch("requests.get", return_value=fake_response):
        with patch("infrastructure.weather_api_client.datetime") as mock_datetime:
            mock_datetime.now.return_value = fake_now

            weather: Weather = client.get_weather(location)

            assert weather.temperature_celsius == 7.2
            assert weather.rain_chance == 90
            assert weather.location == "Berlin"