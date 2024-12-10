with open("input/6", "r") as f:
    lines = f.read().splitlines()

lines = [list(line) for line in lines]


def play() -> int:
    y, x = 93, 71  # start position in my input
    while True:
        print(f"y: {y} x: {x}")
        try:
            match lines[y][x]:
                case "^":
                    if lines[y - 1][x] != "#":
                        lines[y][x] = "X"
                        lines[y - 1][x] = "^"
                        y -= 1
                    else:
                        lines[y][x] = ">"
                case ">":
                    if lines[y][x + 1] != "#":
                        lines[y][x] = "X"
                        lines[y][x + 1] = ">"
                        x += 1
                    else:
                        lines[y][x] = "v"
                case "v":
                    if lines[y + 1][x] != "#":
                        lines[y][x] = "X"
                        lines[y + 1][x] = "v"
                        y += 1
                    else:
                        lines[y][x] = "<"
                case "<":
                    if lines[y][x - 1] != "#":
                        lines[y][x] = "X"
                        lines[y][x - 1] = "<"
                        x -= 1
                    else:
                        lines[y][x] = "^"
        except IndexError:
            break
    return sum(line.count("X") for line in lines) + 1


print(f"part 1: {play()}")
