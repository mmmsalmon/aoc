from itertools import product


def evaluate_left_to_right(nums, ops):
    val = nums[0]
    for i, op in enumerate(ops):
        if op == "+":
            val = val + nums[i + 1]
        elif op == "||":
            val = int(f"{val}" + f"{nums[i + 1]}")
        else:
            val = val * nums[i + 1]
    return val


with open("input/7", "r") as f:
    lines = f.read().strip().splitlines()

correct = []
for line in lines:
    test_val_str, nums_str = line.split(": ")
    test_val = int(test_val_str)
    numbers = list(map(int, nums_str.split()))

    # handle trivial case
    if len(numbers) == 1:
        if numbers[0] == test_val:
            correct.append(test_val)
        continue

    found = False
    for ops in product(["+", "*", "||"], repeat=len(numbers) - 1):
        if evaluate_left_to_right(numbers, ops) == test_val:
            correct.append(test_val)
            found = True
            break

print(f"part 2: {sum(correct)}") # for part 1 remove "||" above
