# === Stage 35: Add active user switching and user-specific records ===
# Project: GearLocker
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"User({self.name!r}, role={self.role!r})"
