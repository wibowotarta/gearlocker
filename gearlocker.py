# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: GearLocker
# gearlocker.py

from datetime import date, timedelta

# --- In-memory data store ---
items = [
    {"id": 1, "name": "Hiking Boots", "borrower": "Alice", "due": date(2025, 8, 15), "condition": "Good", "notes": "Sole slightly worn"},
    {"id": 2, "name": "Climbing Harness", "borrower": "Bob", "due": date(2025, 8, 10), "condition": "Fair", "notes": "Buckle cracked"},
    {"id": 3, "name": "Tent", "borrower": "Charlie", "due": date(2025, 8, 20), "condition": "Excellent", "notes": "All poles intact"},
]

borrowers = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "phone": "555-0101"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "phone": "555-0102"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "phone": "555-0103"},
]

# --- Utility: today's date ---
today = date.today()

# --- Demo: overdue check ---
overdue = [item for item in items if item["due"] < today]
print(f"Today: {today}")
print(f"Overdue items: {len(overdue)}")
for item in overdue:
    print(f"  - {item['name']} (due {item['due']})")
