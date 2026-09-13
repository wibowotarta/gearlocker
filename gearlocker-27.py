# === Stage 27: Add monthly summary calculations ===
# Project: GearLocker
def monthly_summary(records):
    """Compute month-wise checkout counts and total due days."""
    stats = {}
    for r in records:
        key = f"{r['borrower_name']}"
        if key not in stats:
            stats[key] = {"checked_out": 0, "total_due_days": 0}
        stats[key]["checked_out"] += 1
        stats[key]["total_due_days"] += r["due_days"]
    return stats
