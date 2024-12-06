with open("input/2", "r") as f:
    lines = f.readlines()


def isthissafe(x: list) -> list:
    unsafe = []
    for i in x:
        level = list(map(int, i.split(" ")))
        increasing = True
        for n, num in enumerate(level):
            if n == 0:
                continue
            diff = num - level[n - 1]
            if n == 1 and diff < 0:
                increasing = False
            if increasing:
                if not 1 <= diff <= 3:
                    unsafe.append(i)
                    break
            else:
                if not -3 <= diff <= -1:
                    unsafe.append(i)
                    break
        else:
            continue
    return unsafe


unsafelist = isthissafe(lines)
print(f"part 1: {len(lines) - len(unsafelist)}")
#############
unsafelist_new = unsafelist.copy()
for row in unsafelist:
    level = list(map(int, row.split(" ")))
    for n, _ in enumerate(level):
        level_ = level.copy()
        level_.pop(n)
        if not isthissafe([" ".join(map(str, level_))]):
            unsafelist_new.remove(row)
            break
    else:
        continue

# answer is between 391 - 667
print(f"part 2: {len(lines) - len(unsafelist_new)}")
