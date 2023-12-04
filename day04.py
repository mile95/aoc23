with open("input.txt") as f:
    input = f.read().splitlines()


s = 0
for line in input:
    line = line.split(":")[1]
    wns, mns = line.split("|")

    same = set(wns.split()).intersection(set(mns.split()))
    if len(same) > 0:
        s += 2 ** (len(same) - 1)

print(s)


s = 0
rows_won = {i: 1 for i in range(1, len(input) + 1)}

for i, line in enumerate(input, start=1):
    line = line.split(":")[1]
    wns, mns = line.split("|")

    same = set(wns.split()).intersection(set(mns.split()))
    for j in range(i + 1, i + len(same) + 1):
        rows_won[j] = rows_won[j] + rows_won[i]

print(sum(rows_won.values()))
