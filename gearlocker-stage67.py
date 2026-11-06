# === Stage 67: Add a function that returns key project metrics ===
# Project: GearLocker
def get_key_metrics(locker):
    items = locker.get("items", [])
    borrowers = locker.get("borrowers", [])
    total_items = len(items)
    active_borrowers = sum(1 for b in borrowers if b.get("active", False))
    overdue = sum(1 for b in borrowers if b.get("due_date") and b["due_date"] < get_today())
    due_today = sum(1 for b in borrowers if b.get("due_date") and b["due_date"] == get_today())
    returned = sum(1 for b in borrowers if not b.get("active", False))
    checked_out = active_borrowers
    available = total_items - checked_out
    metrics = {
        "total_items": total_items,
        "checked_out": checked_out,
        "available": available,
        "active_borrowers": active_borrowers,
        "returned": returned,
        "overdue": overdue,
        "due_today": due_today,
    }
    return metrics
