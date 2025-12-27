import requests

def fetch_weather(latitude: float, longitude: float, timezone: str) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "current": "temperature_2m,wind_speed_10m,precipitation,precipitation_probability",
    }

    response = requests.get(url, params=params, timeout = 10)
    response.raise_for_status() # This is best practice to ensure we handle HTTP errors
    return response.json()

def summarise_current_weather(weather_data: dict) -> dict:
    current = weather_data["current"]
    return {
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "precipitation": current["precipitation"],
        "precipitation_probability": current["precipitation_probability"],
    }