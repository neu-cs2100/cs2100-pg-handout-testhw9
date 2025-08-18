# FILE: station.py

class Station:
    """Represents a BART station with name and coordinates."""
    
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Station):
            return False
        return self.name == other.name and self.latitude == other.latitude and self.longitude == other.longitude