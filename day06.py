import math

with open("input.txt") as f:
    input = f.read().splitlines()

times = [int(x) for x in input[0].split(":")[1].split()]
distances = [int(x) for x in input[1].split(":")[1].split()]

counts = []
for t, d in zip(times, distances):
    s = 0
    for x in range(0, t + 1):
        c = x * (t - x)
        if c > d:
            s += 1

    counts.append(s)

print(math.prod(counts))


time = int("".join([x for x in input[0].split(":")[1].split()]))
distance = int("".join([x for x in input[1].split(":")[1].split()]))

s = 0
for x in range(0, time + 1):
    c = x * (time - x)
    if c > distance:
        s += 1

print(s)
