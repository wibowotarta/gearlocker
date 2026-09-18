# === Stage 43: Add CSV import for the primary record type ===
# Project: GearLocker
class CSVImporter:
    """Import records from a CSV file into the GearLocker system."""

    @staticmethod
    def import_items(csv_path, delimiter=","):
        """Import items from a CSV file."""
        items = []
        with open(csv_path, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            headers = next(reader)
            for row in reader:
                if len(row) == len(headers):
                    item = Item(
                        name=row[0],
                        category=row[1],
                        condition=row[2],
                    )
                    items.append(item)
        return items

    @staticmethod
    def import_borrowers(csv_path, delimiter=","):
        """Import borrowers from a CSV file."""
        borrowers = []
        with open(csv_path, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            headers = next(reader)
            for row in reader:
                if len(row) == len(headers):
                    borrower = Borrower(
                        name=row[0],
                        email=row[1],
                        phone=row[2],
                    )
                    borrowers.append(borrower)
        return borrowers
