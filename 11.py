with open("input/11", "r") as f:
    line = f.read().split(' ')

def splitstones(input_):
    stones = []
    for stone in input_:
        if stone == '0':
            stones.append('1')
        elif len(stone) % 2 == 0:
            stones.append(stone[:len(stone)//2].lstrip('0'))
            stones.append(stone[len(stone)//2:].lstrip('0'))
        else:
            stones.append(str(int(stone)*2024))
    stones = ['0' if i=='' else i for i in stones]
    return stones


stonelist = splitstones(line)
for i in range(24):
    stonelist = splitstones(stonelist)
    print(len(stonelist))

print(f'part 1: {len(stonelist)}')
