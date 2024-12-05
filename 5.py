with open("input/5", "r") as f:
    lines = f.read().splitlines()

orderrule = [i.rstrip().split("|") for i in lines if "|" in i]
update = [i.rstrip().split(",") for i in lines if "," in i]
correct = []

for row in update:
    incorrect = False
    for x in row:
        choices = [rule for rule in orderrule if x in rule]
        row_no_x = row.copy()
        row_no_x.remove(x)
        choices = [choice for n in row_no_x for choice in choices if n in choice]
        for pair in choices:
            if pair[0] == x:
                if row.index(x) > row.index(pair[1]):
                    incorrect = True
                    break
            else:
                if row.index(pair[0]) > row.index(x):
                    incorrect = True
                    break
        else:
            continue
        break
    if not incorrect:
        correct.append(row)

print(f"part 1: {sum(int(row[int(len(row)/2)]) for row in correct)}")
#############
incorrect = [row for row in update if row not in correct]
# print(incorrect)
