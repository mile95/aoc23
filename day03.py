from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()


def is_valid(x, y, grid) -> bool:
    candidates = [
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
    ]

    for c in candidates:
        try:
            if grid[c[1]][c[0]] != "." and not grid[c[1]][c[0]].isdigit():
                if grid[c[1]][c[0]] == "*":
                    return (True, (c[1], c[0]))
                return (True, None)
        except IndexError:
            pass
    return (False, None)


numbers = []
gear_ratios = 0
gears = defaultdict(list)
for y, row in enumerate(input):
    n = ""
    valids = []
    for x, c in enumerate(row):
        if not c.isdigit():
            if n and any([(v, pos) for (v, pos) in valids if v]):
                gear = [(v, pos) for (v, pos) in valids if v and pos]
                if gear:
                    gears[gear[0][1]].append(int(n))
                numbers.append(int(n))
            n = ""
            valids = []
        else:
            n += c
            valids.append(is_valid(x, y, input))
            if any([(v, pos) for (v, pos) in valids if v]) and x == len(row) - 1:
                gear = [(v, pos) for (v, pos) in valids if v and pos]
                if gear:
                    gears[gear[0][1]].append(int(n))
                numbers.append(int(n))


for k, v in gears.items():
    if len(v) == 2:
        gear_ratios += v[0] * v[1]

print(sum(numbers))
print(gear_ratios)
