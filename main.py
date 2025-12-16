from core.config.config_loader import Config
from core.domains.location import Location
from infrastructure.messengers.telegram_messenger import TelegramMessenger
from infrastructure.weather_api_client import WeatherApiClient
from service.weather_notification_service import WeatherNotificationService
from service.weather_service import WeatherService


def run():
    config = Config.from_files()
    location = Location(name=config.name, latitude=config.latitude, longitude=config.longitude)
    weather_client = WeatherApiClient()
    weather_service = WeatherService(weather_client)
    messenger = TelegramMessenger(chat_id=config.telegram_chat_id, api_token=config.telegram_api_token)
    notification_service = WeatherNotificationService(messenger=messenger, weather_service=weather_service)
    notification_service.run(location=location)


if __name__ == "__main__":
    run()
