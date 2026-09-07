# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: GearLocker
def filter_gearlockers(self, status=None, category=None, owner=None, tag=None):
    results = []
    for locker in self._lockers:
        if status is not None and locker.status != status:
            continue
        if category is not None and locker.category != category:
            continue
        if owner is not None and locker.owner != owner:
            continue
        if tag is not None and tag not in locker.tags:
            continue
        results.append(locker)
    return results
