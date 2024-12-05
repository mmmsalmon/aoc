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


total = sum(
    check(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "X"
)

print(f"part 1: {total}")
