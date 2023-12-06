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


time = ""
distance = ""

for t in times:
    time += str(t)

for d in distances:
    distance += str(d)

time = [int(time)]
distance = [int(distance)]


counts = []
for t, d in zip(time, distance):
    s = 0
    for x in range(0, t + 1):
        c = x * (t - x)
        if c > d:
            s += 1

    counts.append(s)

print(math.prod(counts))
