with open("input.txt") as f:
    lines = f.read().splitlines()

pos = (0, 0)
s1 = 0
s2 = 0
total_meters = 0
for line in lines:
    r, c = pos
    direction, meters, code = line.split()

    total_meters += int(meters)

    if direction == "R":
        change = (1, 0)
    if direction == "D":
        change = (0, 1)
    if direction == "L":
        change = (-1, 0)
    if direction == "U":
        change = (0, -1)

    # https://en.m.wikipedia.org/wiki/Shoelace_formula
    r2, c2 = (r + change[0] * int(meters), c + change[1] * int(meters))
    s1 = s1 + r * c2
    s2 = s2 + c * r2
    pos = (r2, c2)

area = abs(s1 - s2) / 2
print(area + (total_meters / 2) + 1)


pos = (0, 0)
s1 = 0
s2 = 0
total_meters = 0
for line in lines:
    r, c = pos
    _, _, code = line.split()

    code = code.replace("(", "").replace(")", "").replace("#", "")
    meters = int(code[:5], base=16)
    raw_d = code[-1]
    if raw_d == "0":
        direction = "R"
    if raw_d == "1":
        direction = "D"
    if raw_d == "2":
        direction = "L"
    if raw_d == "3":
        direction = "U"

    total_meters += int(meters)

    if direction == "R":
        change = (1, 0)
    if direction == "D":
        change = (0, 1)
    if direction == "L":
        change = (-1, 0)
    if direction == "U":
        change = (0, -1)

    r2, c2 = (r + change[0] * int(meters), c + change[1] * int(meters))
    s1 = s1 + r * c2
    s2 = s2 + c * r2
    pos = (r2, c2)

area = abs(s1 - s2) / 2
print(area + (total_meters / 2) + 1)
