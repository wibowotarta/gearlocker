# === Stage 37: Add recommendations for the next useful action ===
# Project: GearLocker
def generate_due_date_reminders(due_dates, today):
    """Return list of (item, days_overdue) for items past due date."""
    reminders = []
    for item, due in due_dates.items():
        if due < today:
            reminders.append((item, (today - due).days))
    return reminders
