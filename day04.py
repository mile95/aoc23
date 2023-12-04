from collections import defaultdict
with open("input.txt") as f:
    input = f.read().splitlines()

s = 0
for line in input:
    line = line.split(":")[1]
    wns, mns = line.split("|")

    intersection = set(wns.split()) & set(mns.split())
    s += 2 ** (len(intersection) - 1) if len(intersection) > 0 else 0

print(s)

s = 0
d = defaultdict(int)
for i, line in enumerate(input, start=1):
    d[i] += 1
    line = line.split(":")[1]
    wns, mns = line.split("|")
    intersection = set(wns.split()) & set(mns.split())
    for j in range(i + 1, i + len(intersection) + 1):
        d[j] += d[i]

print(sum(d.values()))
