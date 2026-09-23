# === Stage 57: Add structured result objects for command handlers ===
# Project: GearLocker
from dataclasses import dataclass
from typing import Optional


@dataclass
class CheckoutResult:
    """Result of a checkout command."""
    item_id: str
    borrower_id: str
    due_date: str
    condition_note: str
    success: bool = True
    message: str = "Checkout successful"

    def to_dict(self) -> dict:
        return {
            "item_id": self.item_id,
            "borrower_id": self.borrower_id,
            "due_date": self.due_date,
            "condition_note": self.condition_note,
            "success": self.success,
            "message": self.message,
        }


@dataclass
class ReturnResult:
    """Result of a return command."""
    item_id: str
    borrower_id: str
    returned_at: str
    condition_note: str
    success: bool = True
    message: str = "Item returned successfully"

    def to_dict(self) -> dict:
        return {
            "item_id": self.item_id,
            "borrower_id": self.borrower_id,
            "returned_at": self.returned_at,
            "condition_note": self.condition_note,
            "success": self.success,
            "message": self.message,
        }
