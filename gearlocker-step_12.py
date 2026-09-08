# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: GearLocker
def load_data(path):
    """Read JSON file and return parsed data."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in {path}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading {path}: {e}")
        return None
