# === Stage 72: Add Markdown report export ===
# Project: GearLocker
def export_report(locker):
    lines = []
    lines.append("GEARLOCKER REPORT")
    lines.append("GENERATED: " + str(datetime.datetime.now()))
    lines.append("")
    lines.append("ITEMS: " + str(len(locker.items)))
    lines.append("BORROWERS: " + str(len(locker.borrowers)))
    lines.append("")
    lines.append("ACTIVE CHECKOUTS")
    lines.append("-" * 40)
    for item in locker.items:
        for checkout in item.checkouts:
            if checkout.borrower is not None and not checkout.returned:
                due = checkout.due_date.strftime("%Y-%m-%d") if checkout.due_date else "N/A"
                lines.append(item.name + " -> " + checkout.borrower.name + " (due " + due + ")")
    lines.append("")
    lines.append("OVERDUE ITEMS")
    lines.append("-" * 40)
    for item in locker.items:
        for checkout in item.checkouts:
            if checkout.borrower is not None and not checkout.returned and checkout.due_date and checkout.due_date < datetime.datetime.now().date():
                lines.append(item.name + " -> " + checkout.borrower.name + " (overdue by " + str((datetime.datetime.now().date() - checkout.due_date).days) + " days)")
    return "\n".join(lines)
