import random
from datetime import datetime
from pathlib import Path
from datetime import datetime
from src.config import load_config
from src.weather import fetch_weather, summarise_current_weather

def main():
    # Load configuration
    config = load_config()

    # Fetch and summarise weather data
    raw_weather = fetch_weather(
        latitude=config["latitude"],
        longitude=config["longitude"],
        timezone=config["timezone"],
    )
    summary = summarise_current_weather(raw_weather)
    time_now = datetime.now().strftime("%H:%M")

    # Prepare briefing content
    today = datetime.now().strftime("%d %A %B %Y")
    focus = random.choice(config["quotes"])
    briefing_content = (
        f"# Daily Briefing - {today}\n\n"
        f"## Current Conditions\n"
        f"- **Time**: {time_now}\n"
        f"- **Temperature**: {summary['temperature']}°C\n"
        f"- **Wind Speed**: {summary['wind_speed']} km/h\n"
        f"- **Precipitation**: {summary['precipitation']} mm\n"
        f"- **Precipitation Probability**: {summary['precipitation_probability']}%\n"
        f"\n## Focus for today:\n"
        f"- {focus}\n"
    )

    out_path = Path("output/briefing.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(briefing_content, encoding="utf-8")

    print(f"Briefing written to {out_path.resolve()}") # .resolve() converts a relatuve path to an absolute path

if __name__ == "__main__":
    main()
