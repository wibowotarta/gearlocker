# === Stage 19: Add undo support for the last simple mutation ===
# Project: GearLocker
class UndoStack:
    def __init__(self):
        self._history = []

    def push(self, action):
        self._history.append(action)

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()

    def clear(self):
        self._history.clear()
