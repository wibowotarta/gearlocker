# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: GearLocker
def merge_imports(existing_block, new_block):
    existing_lines = [l.strip() for l in existing_block.splitlines() if l.strip()]
    new_lines = [l.strip() for l in new_block.splitlines() if l.strip()]
    merged = []
    for line in existing_lines + new_lines:
        if line.startswith('import ') or line.startswith('from '):
            if not any(_is_dup(l, line) for l in merged):
                merged.append(line)
        else:
            merged.append(line)
    return '\n'.join(merged)


def _is_dup(a, b):
    a_norm = _normalize(a)
    b_norm = _normalize(b)
    if not a_norm or not b_norm:
        return False
    a_names = _extract_names(a)
    b_names = _extract_names(b)
    if not a_names or not b_names:
        return False
    if a_norm == b_norm:
        return True
    if a_norm.startswith('import ') and b_norm.startswith('import '):
        return set(_split_modules(a_norm)) & set(_split_modules(b_norm))
    if a_norm.startswith('from ') and b_norm.startswith('from '):
        return _same_module(a) == _same_module(b) and set(b_names) & set(a_names)
    return False


def _normalize(line):
    line = line.replace(' as ', ' ').replace(',', ' ').replace('(', ' ')
    line = line.replace(')', ' ')
    line = ' '.join(line.split())
    return line


def _split_modules(line):
    modules = set()
    for part in line.split():
        if part.endswith('.') or part.endswith('import '):
            modules.add(part)
    return modules


def _same_module(line):
    if line.startswith('from '):
        return line.split()[1]
    return ''


def _extract_names(line):
    names = set()
    for part in line.replace(', ', ' ').split():
        if part.endswith('.') or part.endswith('import '):
            continue
        if part.endswith(' as '):
            continue
        if part.endswith(')'):
            continue
        if part in ('import', 'from'):
            continue
        names.add(part)
    return names
