from itertools import chain
from math import isqrt
import re

with open("input/13", "r") as f:
    lines = f.read().splitlines()

btn_re = re.compile(r"X\+(\d*), Y\+(\d*)")
machines = []
for line in lines:
    if "A:" in line:
        btn_a = btn_re.findall(line)[0]
    elif "B:" in line:
        btn_b = btn_re.findall(line)[0]
    elif "Prize:" in line:
        prize = re.findall(r"X=(\d*), Y=(\d*)", line)[0]
    else:
        machines.append(
            {
                "btn_a": list(map(int, btn_a)),
                "btn_b": list(map(int, btn_b)),
                "prize": list(map(int, prize)),
            }
        )


def divisors(n):
    return set(
        chain.from_iterable((i, n // i) for i in range(1, isqrt(n) + 1) if n % i == 0)
    )


tokens = []
for claw in machines:  # TODO revert [0] (X for debug)
    div = divisors(claw["prize"][0])
    list_a = {i * claw["btn_a"][0] for i in div}
    list_b = {i * claw["btn_b"][0] for i in div}

    possible_answers = [
        (a, b) for a in list_a for b in list_b if a + b == claw["prize"][0]
    ]

    for a, b in possible_answers:
        pressed_a = (a // claw["btn_a"][0]) * 3
        pressed_b = b // claw["btn_b"][0]
        if pressed_a // 3 <= 100 and pressed_b <= 100:
            tokens.append(pressed_a + pressed_b)

print(f"part 1: {sum(tokens)}")
