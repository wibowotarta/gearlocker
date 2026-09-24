# === Stage 58: Add bulk update behavior for selected records ===
# Project: GearLocker
def bulk_update_records(records, updates):
    """Update multiple records based on selected fields.
    
    Args:
        records: list of record dictionaries to update
        updates: dict of field_name -> new_value
    
    Returns:
        list of updated records
    """
    updated_records = []
    for record in records:
        updated_record = dict(record)
        for field, value in updates.items():
            if field in updated_record:
                updated_record[field] = value
        updated_records.append(updated_record)
    return updated_records
