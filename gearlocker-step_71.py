# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: GearLocker
def seed_demo_data(locker):
    if locker.items:
        return
    locker.add_item("Helmet", "Cycling", "H1")
    locker.add_item("Climbing Rope", "Climbing", "R1")
    locker.add_item("Kayak", "Water Sports", "K1")
    locker.add_borrower("Alice", "alice@example.com")
    locker.add_borrower("Bob", "bob@example.com")
    from datetime import timedelta, datetime
    now = datetime.now()
    due = now + timedelta(days=3)
    locker.check_out("Helmet", "Alice", due, "Minor scratches, no damage")
    due2 = now + timedelta(days=5)
    locker.check_out("Climbing Rope", "Bob", due2, "Good condition")
