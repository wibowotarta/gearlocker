# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: GearLocker
def greet(borrower):
    return f"Welcome back, {borrower}. What would you like to check out today?"


def confirm_return(item, borrower):
    return f"Thanks, {borrower}. {item} has been returned and logged."


def warn_overdue(item, days, borrower):
    return (
        f"Reminder, {borrower}: {item} is {days} day(s) overdue. "
        f"Please return it as soon as possible."
    )


def note_condition(item, condition):
    return f"Condition noted for {item}: {condition}."


def farewell(borrower):
    return f"Have a great day, {borrower}! See you next time."
