# === Stage 36: Add templates for quickly creating common records ===
# Project: GearLocker
def create_quick_records(items=None, borrowers=None):
    """Create common record templates for GearLocker.
    items: list of (name, available) tuples
    borrowers: list of (name, email) tuples
    Returns dict with 'items' and 'borrowers' lists.
    """
    if items is None:
        items = [
            ("Laptop", True),
            ("Headset", True),
            ("Projector", False),
            ("Tripod", True),
            ("Cable Kit", True),
        ]
    if borrowers is None:
        borrowers = [
            ("Alice Johnson", "alice@example.com"),
            ("Bob Smith", "bob@example.com"),
            ("Carol White", "carol@example.com"),
        ]
    return {"items": items, "borrowers": borrowers}
