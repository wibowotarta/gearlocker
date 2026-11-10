# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: GearLocker
CLEAR_FLAG = False


def confirm_clear():
    global CLEAR_FLAG
    CLEAR_FLAG = input("Type 'yes' to confirm clearing the locker: ").strip().lower() == "yes"


def clear_state():
    confirm_clear()
    if not CLEAR_FLAG:
        print("Clearing cancelled. No changes were made.")
        return
    items.clear()
    borrowers.clear()
    notes.clear()
    print("GearLocker cleared. All items, borrowers, and notes removed.")
