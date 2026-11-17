# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: GearLocker
import subprocess


def run_cli(args):
    print("\n$ gearlocker", " ".join(args))
    result = subprocess.run(
        ["python", "gearlocker.py"] + args,
        capture_output=True, text=True
    )
    print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())


run_cli(["list"])
run_cli(["add", "--name", "Climbing Harness", "--category", "Safety", "--qty", "2"])
run_cli(["add", "--name", "Alex Turner", "--email", "alex@example.com"])
run_cli(["checkout", "--item", "Climbing Harness", "--borrower", "Alex Turner", "--days", "3", "--notes", "Minor abrasion on buckle"])
run_cli(["list", "--status", "active"])
run_cli(["overdue"])
run_cli(["return", "--id", "1", "--notes", "Returned in good condition"])
run_cli(["report"])
