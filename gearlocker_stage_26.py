# === Stage 26: Add weekly summary calculations ===
# Project: GearLocker
def weekly_summary(items):
    """Return a dict of weekly checkout counts and average due days."""
    weeks = {}
    for it in items:
        if it.get("checked_out"):
            week = it["checked_out"].isocalendar()[1]
            weeks.setdefault(week, {"checkout": 0, "due_days": []})
            weeks[week]["checkout"] += 1
            if it.get("due_date"):
                try:
                    due = it["due_date"].isocalendar()[1]
                    weeks[week]["due_days"].append(due - week)
                except Exception:
                    pass
    result = {}
    for week, data in weeks.items():
        avg = sum(data["due_days"]) / len(data["due_days"]) if data["due_days"] else 0
        result[week] = {"checkout": data["checkout"], "avg_due_days": round(avg, 1)}
    return result
