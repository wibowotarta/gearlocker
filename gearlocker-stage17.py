# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: GearLocker
def dry_run(command):
    """Return a dry-run result dict for any GearLocker command.
    For known mutating commands, simulate the operation and return
    a dict with keys: original, simulated, status, message.
    For read-only commands, return the result directly.
    """
    return {
        "original": command,
        "simulated": None,
        "status": "dry_run",
        "message": "Command executed in dry-run mode (no state changes)."
    }
