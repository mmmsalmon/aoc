with open("input/4", "r") as f:
    lines = f.read().splitlines()


def check(x: int, y: int) -> int:
    choice = []

    if x + 3 < len(lines[0]):
        choice.append([lines[y][x + i] for i in range(4)])  # >
    if 0 <= x - 3:
        choice.append([lines[y][x - i] for i in range(4)])  # <
    if y + 3 < len(lines):
        choice.append([lines[y + i][x] for i in range(4)])  # v
    if 0 <= y - 3:
        choice.append([lines[y - i][x] for i in range(4)])  # ^

    if x + 3 < len(lines[0]) and y + 3 < len(lines):
        choice.append([lines[y + i][x + i] for i in range(4)])  # ↘
    if 0 <= x - 3 and 0 <= y - 3:
        choice.append([lines[y - i][x - i] for i in range(4)])  # ↖
    if 0 <= x - 3 and y + 3 < len(lines):
        choice.append([lines[y + i][x - i] for i in range(4)])  # ↙
    if x + 3 < len(lines[0]) and 0 <= y - 3:
        choice.append([lines[y - i][x + i] for i in range(4)])  # ↗

    return choice.count(["X", "M", "A", "S"])


total = sum(check(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "X")

print(f"part 1: {total}")


#############
def check2(x: int, y: int) -> int:
    diag, mas = "", 0

    if x + 1 < len(lines[0]) and y + 1 < len(lines):
        diag += lines[y + 1][x + 1]  # ↘
    if 0 <= x - 1 and 0 <= y - 1:
        diag += lines[y - 1][x - 1]  # ↖
    if 0 <= x - 1 and y + 1 < len(lines):
        diag += lines[y + 1][x - 1]  # ↙
    if x + 1 < len(lines[0]) and 0 <= y - 1:
        diag += lines[y - 1][x + 1]  # ↗

    if diag.count("M") == 2 and diag.count("S") == 2 and diag != "SSMM" and diag != "MMSS":
        mas = 1

    return mas


total = sum(check2(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "A")

print(f"part 2: {total}")
