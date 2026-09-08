# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: GearLocker
def case_insensitive_search(self, query, field):
    """Perform a case-insensitive search on the specified field.
    Returns a list of matching records."""
    if not query or not field:
        return self.data
    query_lower = query.lower()
    if field == "item_name":
        search_field = lambda r: r["item_name"].lower()
    elif field == "borrower_name":
        search_field = lambda r: r["borrower_name"].lower()
    elif field == "notes":
        search_field = lambda r: r.get("notes", "").lower()
    elif field == "due_date":
        search_field = lambda r: r.get("due_date", "").lower()
    else:
        search_field = lambda r: str(r.get(field, "")).lower()
    return [r for r in self.data if query_lower in search_field(r)]
