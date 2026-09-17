# === Stage 40: Add plain text report export ===
# Project: GearLocker
def export_report(items, borrowers):
    lines = ["GearLocker Report", "=" * 40]
    for item in items:
        lines.append(f"Item: {item['name']}, Borrowed by: {item['borrower']['name']}, Due: {item['due_date']}")
        if item.get('notes'):
            lines.append(f"  Notes: {item['notes']}")
    lines.append("=" * 40)
    lines.append(f"Total items: {len(items)}, Total borrowers: {len(borrowers)}")
    return "\n".join(lines)
