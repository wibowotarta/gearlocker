# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: GearLocker
def bulk_delete_locked(self, items, confirmed=False):
    if not confirmed:
        raise PermissionError("Bulk delete requires explicit user confirmation.")
    for item in items:
        if item.loaned:
            raise ValueError("Cannot delete items currently checked out.")
        self._items.pop(item.id, None)
    return len(items)
