with open("input/9", "r") as f:
    line = list(map(int, f.read()))

files = line[0::2]
space = line[1::2]
space.append(0)

disk = []
for i in range(len(files)):
    disk.append(str(i)*files[i])
    disk.append('.'*space[i])

# regroup into individual elements
disk = list(''.join(disk))

reserve = [i for i in list(reversed(disk)) if i != '.']
refactored_disk, iter_ = disk.copy(), 0
for n, c in enumerate(disk):
    if c == '.':
        refactored_disk[n] = reserve[iter_]
        try:
            lastnum = int(refactored_disk[list(reversed(refactored_disk)).index(reserve[iter_])])
        except ValueError:
            break
        refactored_disk[-lastnum-1] = '.'
        iter_ += 1
    if ' ' not in ''.join(refactored_disk).replace('.', ' ').strip():
        break

refactored_disk = list(map(int, [i for i in refactored_disk if i != '.']))
res = 0
for n, c in enumerate(refactored_disk):
    res += n*c

print(f'part 1: {res}')
#144236813958 is too low
#93806449939 is too low
