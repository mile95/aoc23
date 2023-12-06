with open("input.txt") as f:
    sections = f.read().split("\n\n")


seeds = [int(x) for x in sections[0].split(":")[1].split()]

for section in sections[1:]:
    lines = section.split("\n")[1:]
    changes = []
    for s in seeds:
        found = False
        for line in lines:
            vals = [int(x) for x in line.split()]
            if not vals:
                continue
            if s >= vals[1] and s < vals[1] + vals[2]:
                offset = s - vals[1]
                changes.append(vals[0] + offset)
                found = True
        if not found:
            changes.append(s)
    seeds = changes

print(min(seeds))


seeds = [int(x) for x in sections[0].split(":")[1].split()]
seeds_with_max_min = []
for s in range(0, len(seeds), 2):
    seeds_with_max_min.append((seeds[s], seeds[s] + seeds[s + 1]))

seeds = seeds_with_max_min
location = 0
done = False
while not done:
    location += 1
    cv = location
    for section in reversed(sections[1:]):
        lines = section.split("\n")[1:]
        found = False
        for line in reversed(lines):
            if found:
                break
            vals = [int(x) for x in line.split()]
            if vals:
                dest_start, source_start, length = vals
                if cv >= dest_start and cv < dest_start + length:
                    offset = cv - dest_start
                    cv = source_start + offset
                    found = True

    for i, (l, u) in enumerate(seeds):
        if cv >= l and cv <= u:
            print(location)
            done = True
