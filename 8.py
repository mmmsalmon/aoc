with open("input/8", "r") as f:
    lines = f.read().splitlines()

lines = [list(line) for line in lines]


def second(c: str, coor1: tuple) -> list:
    coor2list = []
    antinode = False
    for y, line in enumerate(lines):
        if c in line:
            for x, c2 in enumerate(line):
                if c == c2 and (x, y) != coor1:
                    coor2list.append((x, y))

    def withinbounds(coor2: tuple):
        res = False
        coor1x, coor1y = coor1
        coor2x, coor2y = coor2
        distance_x, distance_y = coor2x - coor1x, coor2y - coor1y
        offset_x, offset_y = coor1x - distance_x, coor1y - distance_y
        if 0 <= offset_x <= 50 and 0 <= offset_y <= 50:
            res = True
        return res

    return list(filter(withinbounds, coor2list))


antinode = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            antinode.append(second(c, (x, y)))

antinode = [i for i in antinode if i != []]
antinode = [j for i in antinode for j in i]

print(len(set(antinode)))
# 237 is too low
# 467 is wrong
