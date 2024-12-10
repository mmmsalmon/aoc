with open("input/1", "r") as f:
    lines = f.readlines()

left, right = [], []
for i in lines:
    pair = i.split("   ")
    left.append(int(pair[0]))
    right.append(int(pair[1].strip()))

left.sort()
right.sort()
pairlist = [(i, right[n]) for n, i in enumerate(left)]
difflist = [abs(l - r) for l, r in pairlist]

print(f"part 1: {sum(difflist)}")
#############
similarity = 0
for i in left:
    similarity += i * right.count(i)

print(f"part 2: {similarity}")
