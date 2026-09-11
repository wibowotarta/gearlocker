# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: GearLocker
def archive_and_restore(self, cutoff_days=365):
    """Move completed or old records to an archive, and restore them on demand.

    Records with a status of 'completed' or 'returned' are candidates for archiving.
    Records older than cutoff_days are also archived. Archived records are stored
    in a separate dictionary, and their IDs are removed from the active records.
    On restore, archived records are moved back to the active records.
    """
    now = datetime.now()
    cutoff_date = now - timedelta(days=cutoff_days)

    to_archive = []
    for rec_id, rec in self.records.items():
        if rec.status in ('completed', 'returned') or rec.created < cutoff_date:
            to_archive.append(rec_id)

    for rec_id in to_archive:
        self.archived_records[rec_id] = self.records.pop(rec_id)

    if len(self.archived_records) > 0:
        print(f"Archived {len(to_archive)} records. Total archived: {len(self.archived_records)}")
