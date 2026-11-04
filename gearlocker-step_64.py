# === Stage 64: Add validation for relationship references ===
# Project: GearLocker
def validate_references(data):
    """Validate that all relationship references point to existing records."""
    errors = []
    if not isinstance(data, dict):
        return ["Data must be a dictionary", errors]
    items = data.get("items", [])
    borrowers = data.get("borrowers", [])
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"Item #{index} must be a dictionary")
            continue
        for loan in item.get("loans", []):
            borrower_id = loan.get("borrower_id")
            if borrower_id is None:
                errors.append(f"Item #{index} loan has no borrower_id")
            else:
                valid_borrower_ids = {b.get("id") for b in borrowers if isinstance(b, dict)}
                if borrower_id not in valid_borrower_ids:
                    errors.append(f"Item #{index} loan references unknown borrower_id {borrower_id}")
        owner_id = item.get("owner_id")
        if owner_id is not None and owner_id not in valid_borrower_ids:
            errors.append(f"Item #{index} references unknown owner_id {owner_id}")
    return errors
