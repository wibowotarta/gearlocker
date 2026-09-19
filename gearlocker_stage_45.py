# === Stage 45: Add restore from backup with validation ===
# Project: GearLocker
import json
from pathlib import Path

def restore_backup(backup_path: str, target_path: str) -> bool:
    """Restore target from backup with integrity validation."""
    bp = Path(backup_path)
    if not bp.exists() or bp.stat().st_size == 0:
        return False
    try:
        with bp.open("r", encoding="utf-8") as f:
            data = json.load(f)
        with Path(target_path).open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        return True
    except (json.JSONDecodeError, OSError):
        return False
