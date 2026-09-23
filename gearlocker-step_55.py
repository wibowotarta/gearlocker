# === Stage 55: Add a setting to disable colorized output ===
# Project: GearLocker
import os
import sys


def disable_color_output():
    """Disable colorized terminal output if enabled by environment."""
    if os.environ.get("GEARLOCKER_NO_COLOR", "").lower() in ("1", "true", "yes"):
        os.environ["NO_COLOR"] = "1"
        os.environ["FORCE_COLOR"] = "0"
        try:
            from colorama import deinit, init
            deinit()
            sys.stdout = sys.stderr
        except Exception:
            pass
