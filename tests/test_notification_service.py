from unittest.mock import Mock

from core.domains.location import Location
from service.weather_notification_service import WeatherNotificationService


def test_notification_service():

    location = Location(name="Berlin",longitude=52,latitude=12)

    mock_weather_service = Mock()
    mock_weather_service.get_weather_summary.return_value = "sunny"

    mock_messenger = Mock()
    mock_messenger.send_message.return_value = "A message"

    notification_service = WeatherNotificationService(messenger=mock_messenger,weather_service=mock_weather_service)

    notification_service.run(location=location)

    mock_weather_service.get_weather_summary.assert_called_once_with(location=location)
    mock_messenger.send_message.assert_called_once_with("sunny")


