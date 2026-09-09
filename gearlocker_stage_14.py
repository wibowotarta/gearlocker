# === Stage 14: Add file load support with fallback demo data ===
# Project: GearLocker
import json, os, sys

def load_data(filename="datalocker.json"):
    if os.path.exists(filename):
        with open(filename) as f:
            return json.load(f)
    return {
        "items": [
            {"id": 1, "name": "Helmet", "owner": "Alice", "status": "Checked Out", "notes": "Scratches on left side"},
            {"id": 2, "name": "Gloves", "owner": "Bob", "status": "Available", "notes": ""},
            {"id": 3, "name": "Ski Poles", "owner": "Charlie", "status": "Checked Out", "notes": "One tip bent"}
        ]
    }

if __name__ == "__main__":
    data = load_data()
    print(json.dumps(data, indent=2))
