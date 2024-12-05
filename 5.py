with open("input/5", "r") as f:
    lines = f.read().splitlines()

orderrule = [i.rstrip().split("|") for i in lines if "|" in i]
update = [i.rstrip().split(",") for i in lines if "," in i]


def find(iter_: list) -> list:
    correct = []
    for row in iter_:
        incorrect = False
        for x in row:
            choices = [rule for rule in orderrule if x in rule]
            row_no_x = row.copy()
            row_no_x.remove(x)
            choices = [choice for n in row_no_x for choice in choices if n in choice]
            for pair in choices:
                if (pair[0] == x and row.index(x) > row.index(pair[1])) or (
                    pair[1] == x and row.index(pair[0]) > row.index(x)
                ):
                    incorrect = True
                    break
            else:
                continue
        if not incorrect:
            correct.append(row)
    return correct


def sort(iter_: list) -> list:
    correct = []
    for row in iter_:
        success = False
        while not success:
            success = True
            for x in row:
                choices = [rule for rule in orderrule if x in rule]
                row_no_x = row.copy()
                row_no_x.remove(x)
                choices = [
                    choice for n in row_no_x for choice in choices if n in choice
                ]
                for pair in choices:
                    if pair[0] == x and row.index(x) > row.index(pair[1]):
                        row[row.index(x)], row[row.index(pair[1])] = (
                            row[row.index(pair[1])],
                            row[row.index(x)],
                        )
                        success = False
                    elif pair[1] == x and row.index(pair[0]) > row.index(x):
                        row[row.index(pair[1])], row[row.index(x)] = (
                            row[row.index(x)],
                            row[row.index(pair[1])],
                        )
                        success = False
        if success:
            correct.append(row)
    return correct


correct_list = find(update)
print(f"part 1: {sum(int(row[int(len(row)/2)]) for row in correct_list)}")
#############
incorrect_list = [row for row in update if row not in correct_list]
print(f"part 2: {sum(int(row[int(len(row)/2)]) for row in sort(incorrect_list))}")
