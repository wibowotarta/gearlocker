# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: GearLocker
import re

def validate_positive_integer(value, field_name):
    if not value.isdigit():
        raise ValueError(f"{field_name} must be a positive integer, got '{value}'")
    return int(value)

def validate_short_text(value, field_name, max_length=50):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} is required and must be a non-empty string")
    if len(value) > max_length:
        raise ValueError(f"{field_name} exceeds maximum length of {max_length} characters")
    return value.strip()

def validate_identifier(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty identifier string")
    if not re.match(r'^[A-Za-z0-9_-]+$', value.strip()):
        raise ValueError(f"{field_name} contains invalid characters. Only letters, numbers, hyphens, and underscores are allowed")
    return value.strip()

def validate_due_date(value, field_name):
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a date string in YYYY-MM-DD format")
    try:
        from datetime import datetime
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{field_name} is not a valid date in YYYY-MM-DD format")
    return value
