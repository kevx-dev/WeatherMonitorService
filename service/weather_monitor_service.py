import logging

from core.config.settings import Settings
from core.domains.location import Location
from infrastructure.messengers.telegram_messenger import TelegramMessenger
from infrastructure.weather_api_client import WeatherApiClient
from service.weather_notification_service import WeatherNotificationService
from service.weather_service import WeatherService

logger = logging.getLogger(__name__)


class WeatherMonitorService:

    def __init__(self, settings: Settings):
        self.settings = settings
        self.location = Location(settings.location_name, self.settings.longitude, self.settings.latitude)
        self.weather_api_client = WeatherApiClient()
        self.weather_service = WeatherService(weather_api_client=self.weather_api_client)
        self.messenger = TelegramMessenger(self.settings.telegram_chat_id, self.settings.telegram_api_token)
        self.weather_notification_service = WeatherNotificationService(self.messenger, self.weather_service)

    def run(self):
        logger.info("WeatherMonitorService started")
        try:
            self.weather_notification_service.run(self.location)
            logger.info("WeatherMonitorService finished successfully")
        except Exception:
            logger.error("WeatherMonitorService failed", exc_info=True)
            raise
