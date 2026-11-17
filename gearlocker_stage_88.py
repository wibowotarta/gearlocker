# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: GearLocker
def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_bool(value, default=False):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "y", "t", "on")
    return default


def parse_date(value, default=None):
    if value is None or value == "":
        return default
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            continue
    return default


def parse_condition(value, default="unknown"):
    if value is None:
        return default
    text = str(value).strip().lower()
    for note in ("damaged", "broken", "missing", "unusable"):
        if note in text:
            return note
    for note in ("scratched", "worn", "stained", "dented"):
        if note in text:
            return note
    for note in ("excellent", "pristine", "like new"):
        if note in text:
            return note
    if text == "":
        return default
    return "ok"
