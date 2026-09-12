# === Stage 24: Add grouped summaries by category or status ===
# Project: GearLocker
def grouped_summaries(items):
    """Return a compact dict of summaries grouped by category or status."""
    by_category = {}
    by_status = {}
    for item in items:
        cat = item["category"]
        status = item["status"]
        by_category.setdefault(cat, []).append(item)
        by_status.setdefault(status, []).append(item)
    return {
        "by_category": {cat: len(v) for cat, v in by_category.items()},
        "by_status": {st: len(v) for st, v in by_status.items()},
    }
