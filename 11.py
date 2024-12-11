from time import time
from math import log10, ceil

with open("input/11", "r") as f:
    line = list(map(int, f.read().split(" ")))

starttime = time()


def fastlen(n: int) -> int:
    res = 1
    if n > 0:
        res = int(log10(n)) + 1
    return res


def splitstones(input_):
    stones = []
    for stone in input_:
        if stone == 0:
            stones.append(1)
        elif fastlen(stone) % 2 == 0:
            stone_ = str(stone)
            stones.append(int(stone_[: len(stone_) // 2]))
            stones.append(int(stone_[len(stone_) // 2 :]))
        else:
            stones.append(stone * 2024)
    return stones


stonelist = splitstones(line)
for i in range(74):  # part 1: 24; part 2: 74;
    stonelist = splitstones(stonelist)
    print(f"{i+2}: {len(stonelist)}")

print(f"result: {len(stonelist)}")
print(f"finished in {(time() - starttime):.2f}s")
