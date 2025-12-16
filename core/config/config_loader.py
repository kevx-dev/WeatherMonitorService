import os
from dataclasses import dataclass

import yaml  # type: ignore[import-untyped]
from dotenv import load_dotenv


@dataclass
class Config:
    name: str
    latitude: float
    longitude: float
    telegram_chat_id: str
    telegram_api_token: str

    @classmethod
    def from_files(cls):
        load_dotenv()
        name = os.getenv("LOCATION_NAME")
        latitude = float(os.getenv("LATITUDE"))
        longitude = float(os.getenv("LONGITUDE"))
        telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        telegram_api_token = os.getenv("TELEGRAM_API_TOKEN")

        return cls(name=name, latitude=latitude, longitude=longitude, telegram_chat_id=telegram_chat_id, telegram_api_token=telegram_api_token)
