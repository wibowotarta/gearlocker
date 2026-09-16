# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: GearLocker
def repair_record(record):
    """Fix common data integrity issues in a GearLocker record."""
    if isinstance(record, dict):
        if 'item_id' not in record or not record['item_id']:
            record['item_id'] = 'ITEM-000'
        if 'borrower_name' not in record or not record['borrower_name']:
            record['borrower_name'] = 'Unknown'
        if 'due_date' not in record:
            record['due_date'] = '2024-01-01'
        if 'condition' not in record:
            record['condition'] = 'good'
        if 'returned' not in record:
            record['returned'] = False
        if 'notes' not in record:
            record['notes'] = ''
        return record
    raise TypeError("Expected dict for repair_record")
