# === Stage 83: Add regression tests for the final demo workflow ===
# Project: GearLocker
def test_demo_workflow_end_to_end():
    locker = GearLocker()
    locker.add_item("Climbing Rope", "UIAA 10m single", "New")
    locker.add_item("Helmet", "M", "Scratched")
    bob = locker.register_borrower("Bob", "B123")
    locker.check_out("Climbing Rope", bob, due_days=14, condition="Clean")
    locker.check_out("Helmet", bob, due_days=7, condition="Worn")
    assert locker.items == {"Climbing Rope": "New", "Helmet": "Scratched"}
    assert len(locker.borrowers) == 1
    assert len(locker.checkouts) == 2
    due = locker.next_due("Climbing Rope", bob)
    assert due is not None and due.days == 14
    overdue = locker.overdue("Climbing Rope", bob)
    assert overdue is not None and overdue.days == 14
    locker.return_item("Climbing Rope", bob, condition="Repaired")
    assert locker.items["Climbing Rope"] == "Repaired"
    assert len(locker.checkouts) == 1
    assert len(locker.borrowers) == 1
    assert len(locker.items) == 2
    assert locker.empty_locker() == False
    assert len(locker.locker_stats()) == 3
    assert locker.locker_stats()["total_checkouts"] == 2
    assert locker.locker_stats()["total_returns"] == 1
