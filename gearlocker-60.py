# === Stage 60: Add saved views for frequently used filters ===
# Project: GearLocker
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}
