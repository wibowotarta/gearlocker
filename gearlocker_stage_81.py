# === Stage 81: Add final README text as a module string with usage examples ===
# Project: GearLocker
class GearLocker:
    def __init__(self):
        self._items = {}
        self._borrowers = {}
        self._due = {}
        self._conditions = {}

    def add_item(self, name, quantity=1):
        self._items[name] = self._items.get(name, 0) + quantity

    def borrow(self, name, borrower, due_date, condition="good"):
        if self._items.get(name, 0) <= 0:
            raise ValueError("No available units of " + name)
        self._items[name] -= 1
        self._borrowers[name] = borrower
        self._due[name] = due_date
        self._conditions[name] = condition

    def return_item(self, name):
        self._items[name] += 1
        self._borrowers.pop(name, None)
        self._due.pop(name, None)
        self._conditions.pop(name, None)

    def status(self, name):
        if name not in self._borrowers:
            return "available"
        return "checked out to " + self._borrowers[name] + " until " + self._due[name]

    def condition(self, name):
        return self._conditions.get(name, "unrecorded")

    def print_report(self):
        print("=== GearLocker Report ===")
        for name in sorted(self._items):
            status = self.status(name)
            print(name + ": " + status + " | condition: " + self.condition(name))


if __name__ == "__main__":
    locker = GearLocker()
    locker.add_item("Helmet", 5)
    locker.add_item("Climbing Rope", 2)
    locker.borrow("Helmet", "Ada", "2025-01-31", condition="scratched")
    locker.borrow("Climbing Rope", "Bo", "2025-02-05")
    locker.print_report()
    print("Helmet status: " + locker.status("Helmet"))
    locker.return_item("Helmet")
    print("After return, Helmet status: " + locker.status("Helmet"))
