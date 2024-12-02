with open("input/2", "r") as f:
    lines = f.readlines()

unsafe = []
for i in lines:
    level = list(map(int, i.split(' ')))
    increasing = True
    for n, num in enumerate(level):
        if n == 0:
            continue
        diff = num-level[n-1]
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

#print(len(lines))
#print([val for val in lines if val not in unsafe])
print(f'part 1: {len(lines) - len(unsafe)}')
