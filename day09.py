with open("input.txt") as f:
    lines = f.read().splitlines()

out = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    done = False
    levels = [numbers]
    prev = numbers
    while not done:
        new = []
        for s, e in zip(prev, prev[1:]):
            new.append(e - s)

        prev = new
        levels.append(new)
        if 0 in new and len(set(new)) == 1:
            done = True

    levels = list(reversed(levels))
    for i, level in enumerate(levels):
        if i == 0:
            level.append(0)
        else:
            v = level[-1] + levels[i - 1][-1]
            level.append(v)

    out += levels[-1][-1]

print(out)


out = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    done = False
    levels = [numbers]
    prev = numbers
    while not done:
        new = []
        for s, e in zip(prev, prev[1:]):
            new.append(e - s)

        prev = new
        levels.append(new)
        if 0 in new and len(set(new)) == 1:
            done = True

    levels = list(reversed(levels))
    for i, level in enumerate(levels):
        if i == 0:
            level.append(0)
        else:
            v = level[0] - levels[i - 1][0]
            level.insert(0, v)

    out += levels[-1][0]

print(out)
