# === Stage 53: Add command help text and usage examples ===
# Project: GearLocker
def print_usage():
    print("GearLocker - Equipment Checkout Locker")
    print("Usage:")
    print("  gearlocker.py add_item <name> <qty> <condition> <borrower>")
    print("  gearlocker.py borrow <item_id> <borrower> <due_date>")
    print("  gearlocker.py return_item <item_id>")
    print("  gearlocker.py list_items")
    print("  gearlocker.py list_borrowers")
    print("  gearlocker.py overdue")
    print("  gearlocker.py stats")
    print("  gearlocker.py help")
