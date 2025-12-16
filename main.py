from infrastructure.weather_api_client import WeatherApiClient
from core.domains.location import Location
from service.weather_service import WeatherService
from core.config.config_loader import Config


def run():
    config = Config.from_files()

    location = Location(
        name=config.name,
        latitude=config.latitude,
        longitude=config.longitude
    )
    weather_api_client = WeatherApiClient()
    weather_service = WeatherService(weather_api_client=weather_api_client)

if __name__ == "__main__":
    run()
