with open("input/5", "r") as f:
    lines = f.read().splitlines()

orderrule = [i.rstrip().split("|") for i in lines if "|" in i]
update = [i.rstrip().split(",") for i in lines if "," in i]


def order(iter_: list, mode: str = "find") -> list:
    correct = []
    for row in iter_:
        incorrect, success = False, False
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
                    if pair[0] == x:
                        if row.index(x) > row.index(pair[1]):
                            if mode == "find":
                                incorrect = True
                                break
                            if mode == "sort":
                                row[row.index(x)], row[row.index(pair[1])] = (
                                    row[row.index(pair[1])],
                                    row[row.index(x)],
                                )
                                success = False
                    else:
                        if row.index(pair[0]) > row.index(x):
                            if mode == "find":
                                incorrect = True
                                break
                            if mode == "sort":
                                row[row.index(pair[1])], row[row.index(x)] = (
                                    row[row.index(x)],
                                    row[row.index(pair[1])],
                                )
                                success = False
                else:
                    continue
            if not incorrect and mode == "find":
                correct.append(row)
        if success and mode == "sort":
            correct.append(row)
    return correct


correct_ = order(update)
print(f"part 1: {sum(int(row[int(len(row)/2)]) for row in correct_)}")
#############
incorrect = [row for row in update if row not in correct_]
incorrect_ = order(incorrect, mode="sort")
print(f"part 2: {sum(int(row[int(len(row)/2)]) for row in incorrect_)}")

#part 1: 6034
#part 2: 6305