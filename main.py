from core.config.settings import Settings
from core.logging_setup import setup_logging
from service.weather_monitor_service import WeatherMonitorService


def run():
    setup_logging()
    # noinspection PyArgumentList
    settings = Settings()
    weather_monitor_service = WeatherMonitorService(settings)
    weather_monitor_service.run()



if __name__ == "__main__":
    run()
