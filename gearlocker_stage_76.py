# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: GearLocker
def handle_keyboard_interrupt(signum, frame):
    print("GearLocker interrupted; saving and exiting.")
    try:
        save_state()
    except Exception:
        print("Warning: could not save state.")
    sys.exit(0)


try:
    while True:
        main()
except KeyboardInterrupt:
    handle_keyboard_interrupt(None, None)
