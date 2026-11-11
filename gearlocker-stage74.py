# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: GearLocker
def snapshot_before_after(before, after):
    result = {}
    keys = list(set(list(before.keys()) + list(after.keys())))
    for key in keys:
        result[key] = (before.get(key), after.get(key))
    return result


def diff_records(records, path=None):
    before = {}
    after = {}
    for record in records:
        item = record.get("item")
        borrower = record.get("borrower")
        due = record.get("due_date")
        condition = record.get("condition")
        before[item] = {
            "borrower": borrower,
            "due_date": due,
            "condition": condition,
        }
        after[item] = {
            "borrower": borrower,
            "due_date": due,
            "condition": condition,
        }
    return snapshot_before_after(before, after)


def print_changes(snapshot):
    for key, (old_value, new_value) in snapshot.items():
        if old_value != new_value:
            print("Field: " + key)
            print("  Before: " + str(old_value))
            print("  After:  " + str(new_value))
            print()
