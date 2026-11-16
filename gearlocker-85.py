# === Stage 85: Add final readiness report summarizing features and known limits ===
# Project: GearLocker
def readiness_report(records):
    items = sum(1 for r in records if r["type"] == "item")
    borrowers = sum(1 for r in records if r["type"] == "borrower")
    checked_out = sum(1 for r in records if r["type"] == "checkout")
    overdue = sum(1 for r in records if r["type"] == "checkout" and r["due"] < r["checked_out"])
    lines = [
        "GEARLOCKER READINESS REPORT",
        "=========================",
        "Features:",
        " - Item catalog with condition notes",
        " - Borrower records with join dates",
        " - Checkout events with due dates",
        " - Overdue detection by comparison",
        " - Dependency-free, no external packages",
        "",
        "Summary:",
        " - Items defined: %d" % items,
        " - Borrowers defined: %d" % borrowers,
        " - Checkouts recorded: %d" % checked_out,
        " - Overdue checkouts: %d" % overdue,
        "",
        "Known limits:",
        " - Dates are simple strings, no calendar validation",
        " - No persistence or multi-file merging",
        " - Condition notes are free text, not scored",
        " - No concurrency or user interface",
    ]
    return "\n".join(lines)
