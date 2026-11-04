# === Stage 63: Add relationships between records where useful ===
# Project: GearLocker
class Record:
    def __init__(self, id, name, related=None):
        self.id = id
        self.name = name
        self.related = related or []

    def link(self, other):
        if other not in self.related:
            self.related.append(other)

    def unlink(self, other):
        if other in self.related:
            self.related.remove(other)

    def related_ids(self):
        return [r.id for r in self.related]

items = [
    Record("item-1", "Climbing Rope"),
    Record("item-2", "Helmet"),
    Record("item-3", "Carabiners"),
    Record("item-4", "Crampons"),
]

borrowers = [
    Record("borrower-1", "Alex"),
    Record("borrower-2", "Sam"),
]

links = [
    (items[0], items[1]),
    (items[0], items[2]),
    (items[1], items[3]),
    (items[2], items[3]),
    (items[0], borrowers[0]),
    (items[1], borrowers[1]),
]

for a, b in links:
    a.link(b)
    b.link(a)

for record in items:
    print(f"{record.name} -> {record.related_ids()}")
