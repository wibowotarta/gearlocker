# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: GearLocker
def dispatch(text):
    text = text.strip().lower()
    if text.startswith("add item"):
        return "add_item"
    elif text.startswith("borrow"):
        return "borrow"
    elif text.startswith("return"):
        return "return_item"
    elif text.startswith("status"):
        return "status"
    elif text.startswith("help"):
        return "help"
    else:
        return "unknown"
