# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: GearLocker
def reset_demo_data(gear_locker):
    gear_locker.items = [
        {"id": "1", "name": "Rope 60m", "quantity": 2, "condition": "Good"},
        {"id": "2", "name": "Helmet", "quantity": 5, "condition": "Fair"},
    ]
    gear_locker.borrowers = [
        {"id": "1", "name": "Alice", "item_id": "1", "borrowed_on": "2024-01-01", "due_on": "2024-01-08"},
        {"id": "2", "name": "Bob", "item_id": "2", "borrowed_on": "2024-01-03", "due_on": "2024-01-10"},
    ]
    gear_locker.log = [
        {"action": "reset", "timestamp": "2024-01-15T00:00:00", "message": "Demo data reset."},
    ]
    print("Demo data reset successfully.")
