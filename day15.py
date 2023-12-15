import math
from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().split(",")


def my_hash(s: str) -> int:
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h


s = 0
for line in lines:
    s += my_hash(line)

print(s)

d = defaultdict(list)
for line in lines:
    if "=" in line:
        label, focal = line.split("=")
        operation = "="
    if "-" in line:
        label = line.split("-")[0]
        operation = "-"

    box = my_hash(label)
    if operation == "=":
        found = False
        for i, (l, f) in enumerate(d[box]):
            if label == l:
                d[box][i] = (label, focal)
                found = True
                break
        if not found:
            d[box].append((label, focal))
    if operation == "-":
        for i, (l, f) in enumerate(d[box]):
            if label == l:
                del d[box][i]
                break

s = 0
for k, v in d.items():
    for i, lens in enumerate(v):
        s += math.prod([1 + k, i + 1, int(lens[1])])

print(s)
