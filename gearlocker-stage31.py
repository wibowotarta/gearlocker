# === Stage 31: Add compact table rendering for long lists ===
# Project: GearLocker
def render_compact_table(headers, rows):
    """Render a compact table for long lists, suitable for CLI output."""
    if not headers:
        return ""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    lines = []
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        line = " | ".join(str(c).ljust(col_widths[i]) for i, c in enumerate(row))
        lines.append(line)
    return "\n".join(lines)
