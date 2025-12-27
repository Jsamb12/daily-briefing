import requests

def fetch_weather(latitude: float, longitude: float, timezone: str) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "current": "temperature_2m",
    }

    response = requests.get(url, params=params, timeout = 10)
    response.raise_for_status() # This is best practice to ensure we handle HTTP errors
    return response.json()