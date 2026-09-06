# === Stage 4: Implement create operations for the primary records ===
# Project: GearLocker
class Record:
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at
        }

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at})"
