from unittest.mock import Mock

from core.domains.location import Location
from core.domains.weather import Weather
from service.weather_service import WeatherService


def test_weather_service_logic():
    location = Location(
        name="Berlin",
        longitude=52,
        latitude=12
    )
    fake_client = Mock()
    fake_client.get_weather.return_value = Weather(
        location=location.name,
        temperature_celsius=29,
        rain_chance=89
    )

    service = WeatherService(fake_client)
    assert service.should_take_umbrella(location=location) == True
    assert service.is_today_freezing(location=location) == False
    assert service.get_weather_summary(location=location) == "In Berlin sind es 29 Grad und 89 Prozent Regenwahrscheinlichkeit"
