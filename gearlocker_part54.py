# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: GearLocker
def print_row(data, header=None, sep=" | ", end="\n"):
    if header:
        print(sep.join(f"{x:^12}" for x in header), end=end)
    else:
        print(sep.join(f"{x:^12}" for x in data), end=end)

def print_color(text, color):
    codes = {"red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
             "blue": "\033[94m", "cyan": "\033[96m", "white": "\033[97m", "reset": "\033[0m"}
    return f"{codes.get(color, '')}{text}{codes['reset']}"
