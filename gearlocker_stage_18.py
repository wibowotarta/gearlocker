# === Stage 18: Add an activity log with timestamps and action names ===
# Project: GearLocker
class ActivityLog:
    """Records chronological actions on the locker."""

    def __init__(self):
        self.entries = []

    def log(self, action_name, user, detail=""):
        import datetime
        self.entries.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action_name,
            "user": user,
            "detail": detail,
        })

    def get_log(self):
        return [
            {
                "timestamp": e["timestamp"],
                "action": e["action"],
                "user": e["user"],
                "detail": e["detail"],
            }
            for e in self.entries
        ]
