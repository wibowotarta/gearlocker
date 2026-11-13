# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: GearLocker
def _parse_due_date(raw):
    if raw is None:
        return None
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    return None


def _format_due_date(date):
    return date.strftime("%Y-%m-%d") if date else "None"


def _split_condition_notes(text):
    if not text:
        return []
    return [note.strip() for note in text.split(";") if note.strip()]


def _load_items(path):
    items = []
    if not os.path.exists(path):
        return items
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [piece.strip() for piece in line.split(",")]
            if len(parts) < 4:
                continue
            due = _parse_due_date(parts[3])
            items.append(
                {
                    "name": parts[0],
                    "borrower": parts[1],
                    "due_date": due,
                    "condition_notes": _split_condition_notes(parts[4]),
                }
            )
    return items


def _save_items(path, items):
    with open(path, "w", encoding="utf-8") as handle:
        for item in items:
            handle.write(
                "{name},{borrower},{due},{notes}\n".format(
                    name=item["name"],
                    borrower=item["borrower"],
                    due=_format_due_date(item["due_date"]),
                    notes=";".join(item["condition_notes"]),
                )
            )


def _is_overdue(item, today):
    if not item.get("due_date"):
        return False
    return item["due_date"] < today


def _is_active(item):
    return item.get("borrower") not in (None, "")


def _calculate_overdue_days(item, today):
    if not item.get("due_date"):
        return None
    return (today - item["due_date"]).days


def _add_item(items, name, borrower, due_date, condition_notes):
    return {
        "name": name,
        "borrower": borrower,
        "due_date": _parse_due_date(due_date) if due_date else None,
        "condition_notes": list(condition_notes),
    }
