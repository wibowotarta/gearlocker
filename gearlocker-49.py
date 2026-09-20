# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: GearLocker
import pytest
from datetime import datetime, timedelta

class TestUpdateEdgeCases:
    def test_update_nonexistent_item(self, locker):
        with pytest.raises(ValueError, match="Item not found"):
            locker.update_item("nonexistent", {"name": "new_name"})

    def test_update_with_empty_data(self, locker):
        item = locker.store_item("Test", "Borrower1", datetime.now())
        with pytest.raises(ValueError, match="No fields to update"):
            locker.update_item(item.id, {})

    def test_update_with_invalid_field(self, locker):
        item = locker.store_item("Test", "Borrower1", datetime.now())
        with pytest.raises(ValueError, match="Invalid field"):
            locker.update_item(item.id, {"name": "Test"})

    def test_update_with_invalid_due_date(self, locker):
        item = locker.store_item("Test", "Borrower1", datetime.now())
        with pytest.raises(ValueError, match="Invalid date"):
            locker.update_item(item.id, {"due_date": "not-a-date"})

class TestDeleteEdgeCases:
    def test_delete_nonexistent_item(self, locker):
        with pytest.raises(ValueError, match="Item not found"):
            locker.delete_item("nonexistent")

    def test_delete_empty_locker(self, locker):
        result = locker.delete_item("12345")
        assert result is False

    def test_delete_item_and_verify_removal(self, locker):
        item = locker.store_item("Test", "Borrower1", datetime.now())
        assert locker.get_item(item.id) is not None
        result = locker.delete_item(item.id)
        assert result is True
        assert locker.get_item(item.id) is None

    def test_delete_then_update(self, locker):
        item = locker.store_item("Test", "Borrower1", datetime.now())
        locker.delete_item(item.id)
        with pytest.raises(ValueError, match="Item not found"):
            locker.update_item(item.id, {"name": "Test"})
