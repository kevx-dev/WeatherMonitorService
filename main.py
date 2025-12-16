from core.config.config_loader import Config
from core.domains.location import Location
from infrastructure.messengers.console_messenger import ConsoleMessenger
from infrastructure.messengers.telegram_messenger import TelegramMessenger
from infrastructure.weather_api_client import WeatherApiClient
from service.weather_service import WeatherService


def run():
    config = Config.from_files()

    location = Location(
        name=config.name,
        latitude=config.latitude,
        longitude=config.longitude
    )
    weather_api_client = WeatherApiClient()
    weather_service = WeatherService(weather_api_client=weather_api_client)
    console_messenger = ConsoleMessenger()
    console_messenger.send_message(weather_service.get_weather_summary(location=location))
    telegram_messenger = TelegramMessenger(config.telegram_chat_id,config.telegram_api_token)
    telegram_messenger.send_message(weather_service.get_weather_summary(location=location))
if __name__ == "__main__":
    run()
