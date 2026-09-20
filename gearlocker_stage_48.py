# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: GearLocker
import pytest
from datetime import date
from gearlocker.models import Item, Borrower, Checkout


def test_item_creation():
    item = Item(name="Helmet", sku="H-001", condition="Good")
    assert item.name == "Helmet"
    assert item.sku == "H-001"
    assert item.condition == "Good"


def test_item_validation():
    with pytest.raises(ValueError):
        Item(name="", sku="", condition="")


def test_checkout_creation():
    borrower = Borrower(name="Alice", id="B-001")
    item = Item(name="Helmet", sku="H-001", condition="Good")
    checkout = Checkout(borrower=borrower, item=item, due_date=date(2024, 12, 31))
    assert checkout.borrower.name == "Alice"
    assert checkout.item.name == "Helmet"
    assert checkout.due_date == date(2024, 12, 31)


def test_checkout_validation():
    borrower = Borrower(name="Alice", id="B-001")
    item = Item(name="Helmet", sku="H-001", condition="Good")
    with pytest.raises(ValueError):
        Checkout(borrower=borrower, item=item, due_date=date(2020, 1, 1))
