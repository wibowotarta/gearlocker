# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: GearLocker
def calculate_overdue_days(due_date: datetime.date, today: datetime.date = None) -> int:
    """Return the number of days past the due date, or 0 if not overdue.

    Args:
        due_date: The original due date for the checkout.
        today: Optional reference date. Defaults to today's date.

    Returns:
        Positive integer if overdue, 0 otherwise.
    """
    if today is None:
        today = datetime.date.today()
    delta = today - due_date
    return max(delta.days, 0)

def format_due_date(due_date: datetime.date) -> str:
    """Return a human-readable string representation of a due date.

    Args:
        due_date: The due date to format.

    Returns:
        Formatted date string in 'YYYY-MM-DD' format.
    """
    return due_date.strftime("%Y-%m-%d")

def check_overdue_status(due_date: datetime.date, today: datetime.date = None) -> str:
    """Determine and return the overdue status message for a given due date.

    Args:
        due_date: The original due date for the checkout.
        today: Optional reference date. Defaults to today's date.

    Returns:
        A descriptive string indicating whether the item is on time or overdue.
    """
    if today is None:
        today = datetime.date.today()
    if today <= due_date:
        return "On time"
    else:
        overdue_days = calculate_overdue_days(due_date, today)
        return f"Overdue by {overdue_days} day{'s' if overdue_days != 1 else ''}"
