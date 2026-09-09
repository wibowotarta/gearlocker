# === Stage 16: Add argparse support for the most common commands ===
# Project: GearLocker
import argparse

def main():
    parser = argparse.ArgumentParser(description="GearLocker CLI")
    sub = parser.add_subparsers(dest="command")

    p_item = sub.add_parser("item", help="manage items")
    p_item.add_argument("action", choices=["add", "list", "detail"])
    p_item.add_argument("--name", "-n")
    p_item.add_argument("--serial", "-s")
    p_item.add_argument("--condition", "-c")

    p_borrow = sub.add_parser("borrow", help="borrow items")
    p_borrow.add_argument("action", choices=["add", "list"])
    p_borrow.add_argument("--item", "-i")
    p_borrow.add_argument("--borrower", "-b")
    p_borrow.add_argument("--due", "-d")
    p_borrow.add_argument("--note", "-N")

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()
