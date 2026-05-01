import json
import os 

DATA_FILE = "data/updates.json"

def load_data() -> list[dict]:
    """Reads updates.json and returns a list of update dicts."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data: list[dict]) -> None:
    """Writes the full list of update dicts back to updates.json."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)