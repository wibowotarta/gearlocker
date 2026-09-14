# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: GearLocker
from datetime import date, timedelta

def parse_date(s: str) -> date:
    """Parse a date string in YYYY-MM-DD or YYYY/MM/DD format.
    
    Returns a date object on success.
    Raises ValueError with a clear message on failure.
    """
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return date.fromisoformat(s)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse date '{s}'. Expected YYYY-MM-DD or YYYY/MM/DD.")
