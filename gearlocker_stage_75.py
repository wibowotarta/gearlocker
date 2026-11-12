# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: GearLocker
def generate_validation_report(locker):
    warnings = []
    errors = []

    for item in locker.get_items():
        if item.get_due_date() is None:
            errors.append(f"Item '{item.get_name()}' has no due date.")
        if item.get_condition_note() is None:
            warnings.append(f"Item '{item.get_name()}' has no condition note.")

    for borrower in locker.get_borrowers():
        item = borrower.get_item()
        due_date = borrower.get_due_date()
        if item is None:
            errors.append(f"Borrower '{borrower.get_name()}' is not assigned to any item.")
        elif due_date is None:
            errors.append(f"Borrower '{borrower.get_name()}' has no due date.")
        elif due_date < datetime.now():
            errors.append(f"Borrower '{borrower.get_name()}' is overdue for '{item.get_name()}'.")
        elif due_date - datetime.now() < timedelta(days=1):
            warnings.append(f"Borrower '{borrower.get_name()}' is due tomorrow for '{item.get_name()}'.")

    return {"warnings": warnings, "errors": errors}
