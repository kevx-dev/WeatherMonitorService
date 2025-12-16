from dotenv import load_dotenv
import os
from dataclasses import dataclass
import yaml  # type: ignore[import-untyped]

@dataclass
class Config:

    name: str
    latitude: float
    longitude: float

    @classmethod
    def from_files(cls):
        load_dotenv()
        name = os.getenv("LOCATION_NAME")
        latitude = float(os.getenv("LATITUDE"))
        longitude = float(os.getenv("LONGITUDE"))


        return cls(name=name,latitude=latitude,longitude=longitude)



