# === Stage 20: Add duplicate detection for newly created records ===
# Project: GearLocker
def find_duplicates(records):
    seen = set()
    duplicates = []
    for r in records:
        key = (r.get("item"), r.get("borrower"))
        if key in seen:
            duplicates.append(r)
        else:
            seen.add(key)
    return duplicates
