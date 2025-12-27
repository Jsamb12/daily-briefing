import random
from datetime import datetime
from pathlib import Path
from datetime import datetime
from src.config import load_config
from src.weather import fetch_weather, summarise_current_weather
from src.news import fetch_news

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

    # Quote and time
    today = datetime.now().strftime("%d %A %B %Y")
    focus = random.choice(config["quotes"])

    # Fetch news articles
    try: 
        headlines = fetch_news(
        query=config.get("news_query", "technology OR finance OR UK"), 
        limit=config.get("headlines_limit", 7),
        )
    except Exception as e:
        headlines = []
        news_error = str(e)
    else: 
        news_error = None

    news_lines = ["## Headlines"]
    if headlines:
        for item in headlines: 
            news_lines.append(f"- [{item['title']}]({item['url']})")
        news_lines.append("\n*Headlines provided by The Guardian*\n")
    else: 
        news_lines.append("- Unable to fetch news at this time.")
        if news_error:
            news_lines.append(f"\n_Error: {news_error}_\n")
    news_section = "\n".join(news_lines)

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
        f"\n\n{news_section}\n"
    )

    out_path = Path("output/briefing.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(briefing_content, encoding="utf-8")

    print(f"Briefing written to {out_path.resolve()}") # .resolve() converts a relatuve path to an absolute path

if __name__ == "__main__":
    main()
