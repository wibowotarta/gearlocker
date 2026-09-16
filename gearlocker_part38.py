# === Stage 38: Add data integrity checks for broken references ===
# Project: GearLocker
def check_references(self):
    """Verify that every borrower and item reference is still valid."""
    errors = []
    for checkout in self.checkouts:
        if checkout.borrower_id not in self.borrowers:
            errors.append(f"Checkout {checkout.id} references missing borrower {checkout.borrower_id}")
        if checkout.item_id not in self.items:
            errors.append(f"Checkout {checkout.id} references missing item {checkout.item_id}")
    return errors
