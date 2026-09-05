# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: GearLocker
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Item:
    """Represents an equipment item in the locker."""
    name: str
    item_id: str
    condition: str
    quantity: int
    notes: Optional[str] = None


@dataclass
class Borrower:
    """Represents a person who borrows an item."""
    name: str
    email: str
    phone: Optional[str] = None
    student_id: Optional[str] = None


@dataclass
class Checkout:
    """Represents an item checkout record with due date."""
    item: Item
    borrower: Borrower
    checkout_date: date
    due_date: date
    condition_notes: Optional[str] = None
    returned: bool = False
    return_date: Optional[date] = None
