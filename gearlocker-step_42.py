# === Stage 42: Add CSV export without external dependencies ===
# Project: GearLocker
def export_to_csv(records, output_path):
    """Export checkout records to a CSV file without external dependencies."""
    if not records:
        return
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Borrower', 'Due Date', 'Condition', 'Checked Out At', 'Returned At'])
        for rec in records:
            writer.writerow([rec['item'], rec['borrower'], rec['due_date'],
                             rec['condition'], rec['checked_out_at'], rec['returned_at']])
