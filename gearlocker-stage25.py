# === Stage 25: Add daily summary calculations ===
# Project: GearLocker
class DailySummary:
    def __init__(self, date, total_items, active_items, overdue_items, total_borrowers):
        self.date = date
        self.total_items = total_items
        self.active_items = active_items
        self.overdue_items = overdue_items
        self.total_borrowers = total_borrowers

    def get_active_rate(self):
        if self.total_items == 0:
            return 0.0
        return (self.active_items / self.total_items) * 100

    def get_overdue_rate(self):
        if self.active_items == 0:
            return 0.0
        return (self.overdue_items / self.active_items) * 100

    def __str__(self):
        return (
            f"Date: {self.date} | Total Items: {self.total_items} | Active Items: {self.active_items} | "
            f"Active Rate: {self.get_active_rate():.2f}% | Overdue Rate: {self.get_overdue_rate():.2f}% | "
            f"Total Borrowers: {self.total_borrowers}"
        )
