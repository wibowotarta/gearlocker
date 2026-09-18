# === Stage 44: Add backup creation for the data file ===
# Project: GearLocker
def create_backup(source_path, backup_dir="backups"):
    """Create a timestamped backup copy of the data file."""
    import os, shutil
    from datetime import datetime
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(backup_dir, f"gearlocker_backup_{ts}.csv")
    shutil.copy2(source_path, dst)
    return dst
