from src.config import load_config
from src.weather import fetch_weather

def main():
    config = load_config()
    weather = fetch_weather(
        latitude=config["latitude"],
        longitude=config["longitude"],
        timezone=config["timezone"],
    )

    print("Current Temperature:", weather["current"]["temperature_2m"])


if __name__ == "__main__":
    main()
