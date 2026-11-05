# === Stage 66: Add export of a short status dashboard ===
# Project: GearLocker
def print_status_dashboard(locked):
    total = len(locked['items'])
    checked_out = sum(1 for i in locked['items'] if i['borrowed_by'])
    overdue = [i for i in locked['items'] if i['borrowed_by'] and i['due_date'] < locked['today']]
    print("GEARLOCKER STATUS DASHBOARD")
    print("=" * 30)
    print("Total items: {}".format(total))
    print("Checked out: {}".format(checked_out))
    print("Available:   {}".format(total - checked_out))
    print("Overdue:     {}".format(len(overdue)))
    print("-" * 30)
    print("Overdue items:")
    for i in overdue:
        print("  - {} (borrower: {}, due: {})".format(i['name'], i['borrowed_by'], i['due_date']))
    print("=" * 30)
