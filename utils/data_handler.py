import json
import os

DATA_FILE = "data/updates.json"

def load_data() -> list[dict]:
    """Reads updates.json and returns a list of update dicts."""
    if not os.path.exists(DATA_FILE):
        return []

    content = open(DATA_FILE).read().strip()

    if not content:
        return []

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(
            f"'{DATA_FILE}' contains invalid JSON. "
            "Delete it or fix the syntax to start fresh."
        )

    if not isinstance(data, list):
        raise ValueError(f"'{DATA_FILE}' should contain a list, got {type(data).__name__}.")

    return data


def save_data(data: list[dict]) -> None:
    """Writes the full list of update dicts back to updates.json."""
    if not isinstance(data, list):
        raise TypeError(
            f"Expected a list but got {type(data).__name__}. "
            "Pass the full list of update dicts."
        )

    try:
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except OSError as e:
        raise IOError(
            f"Could not write to '{DATA_FILE}' — {e}. "
            "CCheck that the data/ directory exists and you have write permissions."
        )