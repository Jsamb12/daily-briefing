import json 
from pathlib import Path

def load_config(path: str = "config.json") -> dict: 
    return json.loads(Path(path).read_text(encoding="utf-8"))