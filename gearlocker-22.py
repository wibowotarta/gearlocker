# === Stage 22: Add favorite records and quick favorite listing ===
# Project: GearLocker
# Step 22 – Favorites (quick-listing)
import sqlite3
from datetime import date

def add_favorite(conn, user_id, item_id):
    """Insert (user_id, item_id) into favorites if not already present."""
    cur = conn.execute(
        "INSERT OR IGNORE INTO favorites (user_id, item_id) VALUES (?, ?)",
        (user_id, item_id)
    )
    conn.commit()
    return cur.rowcount > 0

def remove_favorite(conn, user_id, item_id):
    """Remove a specific favorite record; return True if it existed."""
    cur = conn.execute(
        "DELETE FROM favorites WHERE user_id = ? AND item_id = ?",
        (user_id, item_id)
    )
    conn.commit()
    return cur.rowcount > 0

def list_favorites(conn, user_id, limit=50):
    """Return the user's favorite (item_id, item_name, due_date) rows."""
    cur = conn.execute(
        "SELECT item_id, item_name, due_date FROM favorites f "
        "JOIN items i ON f.item_id = i.item_id "
        "WHERE f.user_id = ? ORDER BY due_date DESC LIMIT ?",
        (user_id, limit)
    )
    return cur.fetchall()
