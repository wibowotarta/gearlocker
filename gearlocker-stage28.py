# === Stage 28: Add overdue item detection based on due dates ===
# Project: GearLocker
def detect_overdue(items: list, today: str = None) -> list:
    """Return a list of item dicts whose due date is before today."""
    if today is None:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
    overdue = []
    for item in items:
        due = item.get("due_date", "")
        if due and due < today:
            overdue.append(item)
    return overdue
