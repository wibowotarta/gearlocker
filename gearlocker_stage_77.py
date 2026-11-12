# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: GearLocker
def get_borrower_count() -> int:
    return len(BORROWERS)


def get_item_count() -> int:
    return len(ITEMS)


def find_item_by_id(item_id: str) -> Optional[dict]:
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    return None


def find_borrower_by_id(borrower_id: str) -> Optional[dict]:
    for borrower in BORROWERS:
        if borrower["id"] == borrower_id:
            return borrower
    return None


def get_items() -> List[dict]:
    return ITEMS


def get_borrowers() -> List[dict]:
    return BORROWERS


def get_due_items() -> List[dict]:
    today = date.today()
    return [item for item in ITEMS if item["due_date"] <= today]


def get_overdue_items() -> List[dict]:
    today = date.today()
    return [item for item in ITEMS if item["due_date"] < today]


def get_items_by_condition(condition: str) -> List[dict]:
    return [item for item in ITEMS if item["condition"] == condition]


def get_items_by_borrower(borrower_id: str) -> List[dict]:
    return [item for item in ITEMS if item["borrower_id"] == borrower_id]


def get_items_by_due_date_range(start_date: str, end_date: str) -> List[dict]:
    return [
        item for item in ITEMS
        if start_date <= item["due_date"] <= end_date
    ]


def get_items_by_due_date_range(start_date: str, end_date: str) -> List[dict]:
    return [
        item for item in ITEMS
        if start_date <= item["due_date"] <= end_date
    ]


def get_items_by_due_date_range(start_date: str, end_date: str) -> List[dict]:
    return [
        item for item in ITEMS
        if start_date <= item["due_date"] <= end_date
    ]
