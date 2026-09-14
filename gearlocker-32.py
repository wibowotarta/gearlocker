# === Stage 32: Add pagination helpers for long console output ===
# Project: GearLocker
def paginate_output(lines, page_size=10, max_pages=3):
    """Print lines in fixed-size pages for long console output."""
    total = len(lines)
    if total <= page_size:
        print('\n'.join(lines))
        return
    for p in range(max_pages):
        start = p * page_size
        end = start + page_size
        chunk = lines[start:end]
        if not chunk:
            break
        print(f'\n--- Page {p + 1} ---')
        print('\n'.join(chunk))
        if end >= total:
            break
    if total > page_size * max_pages:
        print(f'\n... (truncated: {total - page_size * max_pages} more lines)')
