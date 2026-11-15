# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: GearLocker
def demo_end_to_end():
    locker = {}
    locker["Item 1"] = {"borrower": "Alice", "due": "2025-12-31", "condition": "clean"}
    locker["Item 2"] = {"borrower": "Bob", "due": "2025-11-15", "condition": "scratched"}
    overdue = []
    for item, data in locker.items():
        if data["due"] < "2025-12-01":
            overdue.append(item)
    print("Overdue items:", overdue)
    locker["Item 3"] = {"borrower": "Carol", "due": "2026-01-10", "condition": "new"}
    print("Total items:", len(locker))
    return locker
