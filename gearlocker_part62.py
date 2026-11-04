# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: GearLocker
def recommend_next(items, priority_field="priority", priority_value=0):
    available = [i for i in items if i.get("status") == "available" and i.get("condition") == "good"]
    if not available:
        return []
    return sorted(available, key=lambda i: i.get(priority_field, priority_value), reverse=True)


def score_items(items):
    scored = []
    for i in items:
        base = 1
        if i.get("condition") == "good":
            base += 1
        if i.get("priority", 0) > 0:
            base += i["priority"]
        if i.get("category") in ("safety", "critical"):
            base += 2
        if not i.get("due_date"):
            base += 1
        scored.append((base, i))
    return sorted(scored, key=lambda x: x[0], reverse=True)


def suggest_renewals(borrowers, days_before_due=3):
    suggestions = []
    for b in borrowers:
        due = b.get("due_date")
        if due and due <= get_current_date() + timedelta(days=days_before_due):
            suggestions.append({"borrower": b["name"], "item": b.get("item"), "due": due})
    return suggestions
