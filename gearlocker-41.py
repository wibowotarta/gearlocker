# === Stage 41: Add plain text import for a simple line-based format ===
# Project: GearLocker
def load_csv(path):
    """Read a simple CSV of items: name, borrower, due_date, condition."""
    items = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) == 4:
                items.append({
                    "name": parts[0],
                    "borrower": parts[1],
                    "due_date": parts[2],
                    "condition": parts[3],
                })
    return items
