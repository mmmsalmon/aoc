from re import findall, sub

with open("input/3", "r") as f:
    lines = f.readlines()

mullist = []
for i in lines:
    mullist += findall(r"mul\(\d*,\d*\)", i)
    mullist = [sub(r"mul\(|\)", "", j) for j in mullist]


def findtotal(muls: list) -> int:
    total = 0
    for i in muls:
        x, y = i.split(",")
        total += int(x) * int(y)
    return total


print(f"part 1: {findtotal(mullist)}")
#############
mullist = []
for i in lines:
    mullist += findall(r"(mul\(\d*,\d*\))|(do\(\))|(don\'t\(\))", i)

mullist2, do = [], True
for i in mullist:
    if i[2]:
        do = False
    elif i[1]:
        do = True
    else:
        if do:
            mullist2.append(i[0])

for i in mullist2:
    mullist2 = [sub(r"mul\(|\)", "", j) for j in mullist2]

print(f"part 2: {findtotal(mullist2)}")
