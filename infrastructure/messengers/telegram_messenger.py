import requests  # type: ignore[import-untyped]

from core.protocols.protocols import MessengerProtocol


class TelegramMessenger(MessengerProtocol):

    def __init__(self, chat_id: str, api_token: str):
        self.chat_id: str = chat_id
        self.api_token: str = api_token

    def send_message(self, message: str) -> None:
        BASE_URL: str = f"https://api.telegram.org/bot{self.api_token}/sendMessage"
        payload: dict[str, str] = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }

        response = requests.post(BASE_URL, data=payload)
        response.raise_for_status()
