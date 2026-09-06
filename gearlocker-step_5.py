# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: GearLocker
def update_item(item_id, updates):
    """Update an existing item's fields. Returns a dict with result and message."""
    if item_id not in items:
        return {"result": "error", "message": f"Item {item_id} not found"}
    for key, value in updates.items():
        if key not in item_schema:
            return {"result": "error", "message": f"Unknown field '{key}'"}
        items[item_id][key] = value
    return {"result": "ok", "message": f"Item {item_id} updated"}

def update_borrower(borrower_id, updates):
    """Update an existing borrower's fields. Returns a dict with result and message."""
    if borrower_id not in borrowers:
        return {"result": "error", "message": f"Borrower {borrower_id} not found"}
    for key, value in updates.items():
        if key not in borrower_schema:
            return {"result": "error", "message": f"Unknown field '{key}'"}
        borrowers[borrower_id][key] = value
    return {"result": "ok", "message": f"Borrower {borrower_id} updated"}

def update_loan(loan_id, updates):
    """Update an existing loan's fields. Returns a dict with result and message."""
    if loan_id not in loans:
        return {"result": "error", "message": f"Loan {loan_id} not found"}
    for key, value in updates.items():
        if key not in loan_schema:
            return {"result": "error", "message": f"Unknown field '{key}'"}
        loans[loan_id][key] = value
    return {"result": "ok", "message": f"Loan {loan_id} updated"}
