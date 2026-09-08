# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: GearLocker
def sort_records(records, key="title"):
    """Sort records by title, date, priority, or last update time."""
    order = {"title": 0, "date": 1, "priority": 2, "last_update": 3}
    return sorted(records, key=lambda r: (order.get(key, 0), r.get(key, "")))
