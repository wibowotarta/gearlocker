# === Stage 50: Add unit tests for import and export behavior ===
# Project: GearLocker
import unittest
from datetime import date, timedelta

# Minimal test harness for GearLocker import/export behavior
# Assumes the following classes exist in the project (adapt names if needed):
#   - Item (with: name, borrower, due_date, condition_notes)
#   - Borrower (with: name, email)
#   - Locker (with: items, add_item, checkout, return_item methods)
#   - Exporter (with: to_csv, to_json methods)
#   - Importer (with: from_csv, from_json methods)

class TestGearLockerImportExport(unittest.TestCase):
    def setUp(self):
        self.borrower = Borrower(name="Alice", email="alice@example.com")
        self.item = Item(name="Helmet", borrower=self.borrower, due_date=date.today() + timedelta(days=30), condition_notes="Good")
        self.lk = Locker()
        self.lk.add_item(self.item)
        self.exporter = Exporter()
        self.importer = Importer()

    def test_export_import_csv(self):
        csv_data = self.exporter.to_csv(self.lk)
        imported_lk = self.importer.from_csv(csv_data)
        self.assertEqual(len(imported_lk.items), 1)
        self.assertEqual(imported_lk.items[0].name, "Helmet")
        self.assertEqual(imported_lk.items[0].borrower.name, "Alice")

    def test_export_import_json(self):
        json_data = self.exporter.to_json(self.lk)
        imported_lk = self.importer.from_json(json_data)
        self.assertEqual(len(imported_lk.items), 1)
        self.assertEqual(imported_lk.items[0].name, "Helmet")
        self.assertEqual(imported_lk.items[0].condition_notes, "Good")

    def test_round_trip_preserves_due_date(self):
        csv_data = self.exporter.to_csv(self.lk)
        imported_lk = self.importer.from_csv(csv_data)
        self.assertEqual(imported_lk.items[0].due_date, self.item.due_date)

if __name__ == "__main__":
    unittest.main()
