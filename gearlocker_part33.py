# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: GearLocker
def get_settings():
    return {
        "max_items_per_borrower": 5,
        "default_due_days": 30,
        "late_fee_per_day": 0.5,
        "condition_note_required": True,
        "allow_overdue": False,
        "notification_on_due": True,
    }

def update_settings(settings, updates):
    for key, value in updates.items():
        if key not in settings:
            raise ValueError(f"Unknown setting: {key}")
        settings[key] = value
    return settings
