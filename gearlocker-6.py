# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: GearLocker
def delete_item(item_id: str, confirm: bool = False) -> str:
    """Remove an item from the locker by ID.
    
    Args:
        item_id: Unique identifier of the item to delete.
        confirm: If True, prints a confirmation message before deletion.
    
    Returns:
        A message describing the outcome of the deletion.
    """
    if item_id not in items:
        return f"Item '{item_id}' not found."
    if confirm:
        print(f"Confirming deletion of item '{item_id}'. Proceeding...")
    del items[item_id]
    return f"Item '{item_id}' successfully deleted."
