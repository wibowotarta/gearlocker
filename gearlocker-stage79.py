# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: GearLocker
def self_check(gear):
    print("=== GearLocker self-check ===")
    assert all(i.item_id for i in gear["items"]), "items missing id"
    assert all(b.borrower_id for b in gear["borrowers"]), "borrowers missing id"
    assert all(d["due_date"] for d in gear["checkouts"]), "checkouts missing due_date"
    assert all(c.get("condition") for c in gear["conditions"]), "conditions missing note"
    for c in gear["checkouts"]:
        assert c["due_date"] >= "2000-01-01"
    print("validations passed")
    for i in gear["items"]:
        total = sum(1 for c in gear["checkouts"] if c["item_id"] == i["item_id"])
        print(f"{i['item_id']} active checkouts: {total}")
    overdue = [c["checkout_id"] for c in gear["checkouts"] if c["due_date"] < "2000-01-01"]
    if overdue:
        print("overdue checkouts:", overdue)
    else:
        print("no overdue checkouts")
    print("self-check complete")
