# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: GearLocker
def remove_unused_helpers(collection, keep=None):
    keep = keep or set()
    names = set(dir(collection)) - {'__all__'}
    for name in list(names):
        if name.startswith('_'):
            continue
        if name in keep:
            continue
        try:
            obj = getattr(collection, name)
        except AttributeError:
            continue
        used = False
        for item in collection.values():
            if hasattr(item, name) or name in dir(item):
                used = True
                break
        if not used and not callable(obj):
            try:
                delattr(collection, name)
            except AttributeError:
                pass


def normalize_due_date(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return value
    try:
        return datetime.date.fromisoformat(str(value).strip())
    except (ValueError, TypeError):
        return None


def merge_condition_notes(existing, new_note):
    if not existing:
        return new_note
    if not new_note:
        return existing
    if new_note.startswith('Replaced:'):
        return new_note
    return existing + ' | ' + new_note


def dedupe_by_name(items):
    seen = set()
    result = []
    for item in items:
        key = item.get('name')
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result
