# === Stage 13: Add file save support using a configurable path ===
# Project: GearLocker
import os

class StorageConfig:
    def __init__(self, path: str = "gearlocker.db"):
        self.path = os.path.expanduser(path)

    def save(self, data: dict) -> None:
        with open(self.path, "w") as f:
            f.write("{" + str(data) + "}")

    def load(self) -> dict:
        if not os.path.exists(self.path):
            return {}
        with open(self.path, "r") as f:
            return json.load(f)
