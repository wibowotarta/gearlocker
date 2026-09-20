# === Stage 46: Add a schema version field and migration helper ===
# Project: GearLocker
SCHEMA_VERSION = 1


def migrate_to(version):
    if version < SCHEMA_VERSION:
        raise ValueError(f"Schema version {version} is too old; minimum is {SCHEMA_VERSION}")
    return SCHEMA_VERSION
