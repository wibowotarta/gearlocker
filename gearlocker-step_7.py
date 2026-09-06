# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: GearLocker
def format_item(item: dict) -> str:
    return f"{item['id']}. {item['name']} (ID: {item['item_id']})"

def format_borrower(borrower: dict) -> str:
    return f"{borrower['name']} (ID: {borrower['borrower_id']})"

def format_due(due: dict) -> str:
    status = "Overdue!" if due['status'] == 'overdue' else due['status'].capitalize()
    return f"Due: {due['due_date']} — {status}"

def format_condition(cond: dict) -> str:
    return f"Condition: {cond['notes']}"

def format_borrow_log(log: dict) -> str:
    return f"{log['borrower']} borrowed {log['item']} on {log['borrow_date']}"
