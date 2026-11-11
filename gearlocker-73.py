# === Stage 73: Add a lightweight HTML report export ===
# Project: GearLocker
def export_report(projects, items, borrowers, checkouts, condition_notes, output_path):
    with open(output_path, "w") as f:
        f.write("GEARLOCKER EQUIPMENT CHECKOUT REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write("ITEMS\n")
        f.write("-" * 40 + "\n")
        for item in items:
            f.write(f"ID: {item['id']} | Name: {item['name']}\n")
        f.write("\nBORROWERS\n")
        f.write("-" * 40 + "\n")
        for borrower in borrowers:
            f.write(f"ID: {borrower['id']} | Name: {borrower['name']}\n")
        f.write("\nCHECKOUTS\n")
        f.write("-" * 40 + "\n")
        for checkout in checkouts:
            f.write(
                f"ID: {checkout['id']} | Item: {checkout['item_id']} | "
                f"Borrower: {checkout['borrower_id']} | Due: {checkout['due_date']}\n"
            )
            note = condition_notes.get(checkout['id'])
            if note:
                f.write(f"Condition: {note}\n")
        f.write("\nEND OF REPORT\n")
