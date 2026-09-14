# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: GearLocker
def get_upcoming_items(locked_items, days_ahead=14):
    """Return items whose due date is within the next N days, sorted earliest first."""
    today = datetime.now()
    return sorted(
        [item for item in locked_items if item["due_date"] >= today],
        key=lambda i: i["due_date"]
    )
