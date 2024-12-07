from itertools import combinations_with_replacement

with open("input/7", "r") as f:
    lines = f.read().splitlines()

correct = []
for line in lines:
    line = line.split(": ")
    line[1] = line[1].split(" ")
    operationlist = list(combinations_with_replacement({"*", "+"}, len(line[1]) - 1))
    operationlist = [[*op] for op in operationlist]
    for op in operationlist:
        op.append("")
    for op in operationlist:
        pre = list(zip(line[1], op))
        res = "".join(["".join(i) for i in pre])
        ans = eval(res)
        if ans == int(line[0]):
            correct.append(ans)

print(f"part 1: {sum(correct)}")
# 35617161571 is too low
