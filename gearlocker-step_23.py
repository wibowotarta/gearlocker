# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: GearLocker
def toggle_tag(item, tag_name):
    """Add tag if absent, remove if present."""
    if tag_name in item.tags:
        item.tags.remove(tag_name)
    else:
        item.tags.append(tag_name)

def tag_summary(items, tag_name):
    """Return count and list of items matching a tag."""
    return [it for it in items if tag_name in it.tags]
