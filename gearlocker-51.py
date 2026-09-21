# === Stage 51: Add unit tests for search and filter behavior ===
# Project: GearLocker
class TestGearLocker(unittest.TestCase):
    def setUp(self):
        self.locker = GearLocker("TestLocker")

    def test_search_by_name(self):
        self.locker.add_item(Item("Rope", "Good", "Alice", datetime(2025, 1, 1)))
        self.locker.add_item(Item("Helmet", "Damaged", "Bob", datetime(2025, 1, 2)))
        self.locker.add_item(Item("Rope", "Good", "Charlie", datetime(2025, 1, 3)))
        results = self.locker.search("Rope")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].name, "Rope")
        self.assertEqual(results[1].name, "Rope")

    def test_filter_by_due_date(self):
        self.locker.add_item(Item("Rope", "Good", "Alice", datetime(2025, 1, 1)))
        self.locker.add_item(Item("Helmet", "Good", "Bob", datetime(2025, 12, 31)))
        self.locker.add_item(Item("Gloves", "Good", "Charlie", datetime(2025, 6, 15)))
        due_items = self.locker.filter_by_due_date(datetime(2025, 6, 16))
        self.assertEqual(len(due_items), 2)
        self.assertEqual(due_items[0].name, "Gloves")
        self.assertEqual(due_items[1].name, "Rope")

    def test_filter_by_due_date_returns_all(self):
        self.locker.add_item(Item("Rope", "Good", "Alice", datetime(2025, 1, 1)))
        self.locker.add_item(Item("Helmet", "Good", "Bob", datetime(2025, 12, 31)))
        due_items = self.locker.filter_by_due_date(datetime(2024, 1, 1))
        self.assertEqual(len(due_items), 2)

    def test_search_returns_empty(self):
        self.locker.add_item(Item("Rope", "Good", "Alice", datetime(2025, 1, 1)))
        results = self.locker.search("NonExistent")
        self.assertEqual(len(results), 0)

    def test_filter_by_due_date_returns_empty(self):
        self.locker.add_item(Item("Rope", "Good", "Alice", datetime(2025, 1, 1)))
        due_items = self.locker.filter_by_due_date(datetime(2026, 1, 1))
        self.assertEqual(len(due_items), 0)
