# === Stage 56: Add compact error classes for domain failures ===
# Project: GearLocker
class GearLockerError(Exception):
    pass

class ItemNotFoundError(GearLockerError):
    pass

class BorrowerNotFoundError(GearLockerError):
    pass

class DueDateError(GearLockerError):
    pass

class ConditionNoteError(GearLockerError):
    pass
