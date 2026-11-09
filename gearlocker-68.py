# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: GearLocker
def generate_changelog(activity_log, limit=20):
    entries = activity_log[-limit:] if len(activity_log) > limit else list(reversed(activity_log))
    lines = []
    for entry in entries:
        date = entry.get("date", "Unknown")
        action = entry.get("action", "unknown")
        detail = entry.get("detail", "")
        if detail:
            lines.append(f"- {date}: {action} {detail}")
        else:
            lines.append(f"- {date}: {action}")
    header = "=== GearLocker Changelog ==="
    if entries:
        header += f"\nGenerated from {len(entries)} activity entries"
    return "\n".join([header] + lines)
