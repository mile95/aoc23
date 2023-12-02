with open("input.txt") as f:
    input = f.read().splitlines()

s = 0
for i, game in enumerate(input):
    records = [g.split() for g in game.split(":")[1].split(":")]
    valid = True
    for record in records:
        record = [(record[i], record[i + 1]) for i in range(0, len(record), 2)]
        for n, c in record:
            if "blue" in c:
                valid = valid and int(n) <= 14
            if "red" in c:
                valid = valid and int(n) <= 12
            if "green" in c:
                valid = valid and int(n) <= 13

        s += i + 1 if valid else 0
print(s)


s = 0
for i, game in enumerate(input):
    records = [g.split() for g in game.split(":")[1].split(":")]
    mr = mb = mg = 0
    for record in records:
        record = [(record[i], record[i + 1]) for i in range(0, len(record), 2)]
        for n, c in record:
            if "blue" in c:
                mb = max(mb, int(n))
            if "red" in c:
                mr = max(mr, int(n))
            if "green" in c:
                mg = max(mg, int(n))
    s += mr * mb * mg
print(s)
