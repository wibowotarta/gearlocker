# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: GearLocker
def _normalize_report(report):
    normalized = {}
    for entry in report:
        key = (entry.get("id"), entry.get("borrower"), entry.get("due_date"), entry.get("condition"))
        normalized[key] = entry
    return normalized


def compare_reports(report_a, report_b):
    normalized_a = _normalize_report(report_a)
    normalized_b = _normalize_report(report_b)

    keys = set(normalized_a.keys()) | set(normalized_b.keys())

    added = []
    removed = []
    changed = []

    for key in sorted(keys):
        in_a = key in normalized_a
        in_b = key in normalized_b

        if in_a and not in_b:
            removed.append(key)
        elif in_b and not in_a:
            added.append(key)
        else:
            entry_a = normalized_a[key]
            entry_b = normalized_b[key]
            if entry_a != entry_b:
                changed.append(key)

    return {"added": added, "removed": removed, "changed": changed}


def report_changed_count(report_a, report_b):
    result = compare_reports(report_a, report_b)
    return len(result["added"]) + len(result["removed"]) + len(result["changed"])
