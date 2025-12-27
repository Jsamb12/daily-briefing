import os 
import requests
from dotenv import load_dotenv

def fetch_news(query: str, limit: int = 7) -> list[dict]:
    load_dotenv()

    api_key = os.getenv("GUARDIAN_API_KEY")
    if not api_key:
        raise ValueError("GUARDIAN_API_KEY not found in environment variables")
    
    url = "https://content.guardianapis.com/search"
    params = {
        "q": query,
        "page-size": limit,
        "order-by": "newest",
        "api-key": api_key
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    results = r.json()["response"]["results"]
    return [{"title": item["webTitle"], "url": item["webUrl"]} for item in results]