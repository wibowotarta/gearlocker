# === Stage 34: Add support for multiple local user profiles ===
# Project: GearLocker
import json
import os

PROFILES_DIR = "profiles"

def _ensure_dir():
    os.makedirs(PROFILES_DIR, exist_ok=True)

def load_all_profiles():
    _ensure_dir()
    profiles = {}
    for fname in os.listdir(PROFILES_DIR):
        if fname.endswith(".json"):
            path = os.path.join(PROFILES_DIR, fname)
            with open(path) as f:
                profiles[fname[:-5]] = json.load(f)
    return profiles

def save_profile(name, data):
    _ensure_dir()
    path = os.path.join(PROFILES_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path
