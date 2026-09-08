# === Stage 11: Add JSON export for the current application state ===
# Project: GearLocker
import json

def export_state(lenders, borrowers, checkouts):
    """Export the full GearLocker state to a JSON string."""
    state = {
        "lenders": {id_: {"name": l.name, "email": l.email} for id_, l in lenders.items()},
        "borrowers": {id_: {"name": b.name, "email": b.email} for id_, b in borrowers.items()},
        "checkouts": [
            {
                "id": c.id,
                "item": c.item_id,
                "borrower_id": c.borrower_id,
                "borrower_name": c.borrower.name,
                "due_date": c.due_date,
                "condition": c.condition,
                "notes": c.notes,
                "checked_out_at": c.checked_out_at,
                "returned": c.returned,
            }
            for c in checkouts
        ],
    }
    return json.dumps(state, indent=2)
