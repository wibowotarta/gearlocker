# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: GearLocker
# GearLocker Demo Scenario
# Demonstrates the core workflow: add items, borrow them, and check status.

from gear_locker.models import Item, Borrower
from gear_locker.services import Locker

# Initialize the locker
locker = Locker()

# Add items
hammer = Item(name="Hammer", borrower_id=None, due_date=None, condition_note="Good")
screwdriver = Item(name="Screwdriver Set", borrower_id=None, due_date=None, condition_note="Functional")
wrench = Item(name="Adjustable Wrench", borrower_id=None, due_date=None, condition_note="Needs cleaning")

locker.add_item(hammer)
locker.add_item(screwdriver)
locker.add_item(wrench)

# Create borrowers
alice = Borrower(name="Alice", role="member")
bob = Borrower(name="Bob", role="member")

# Borrow items
locker.borrow_item(hammer, alice)
locker.borrow_item(screwdriver, bob)

# Simulate overdue scenario
import datetime
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
locker.set_due_date(screwdriver, tomorrow)

# Check status
print("Current Locker Status:")
locker.display_status()

# List all items
print("\nAll Items in Locker:")
locker.list_items()

# List all borrowers
print("\nAll Borrowers:")
locker.list_borrowers()
