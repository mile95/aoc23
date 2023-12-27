from copy import deepcopy

with open("input.txt") as f:
    patterns = f.read().split("\n\n")

s = 0

# Map each pattern with the mirror index so that this can be ignored
# when searching for part B solution.
d = {}
for k, pattern in enumerate(patterns):
    lines = pattern.splitlines()
    G = [[x for x in line] for line in lines]
    H = len(G)
    W = len(G[0])
    # row by row
    for i, (r1, r2) in enumerate(list(zip(G, G[1:]))):
        if r1 == r2:
            to_low = i
            to_max = H - i - 2
            valid = True
            for off in range(1, min(to_low, to_max) + 1):
                valid = valid and G[i - off] == G[i + 1 + off]
            if valid:
                mirror = i
                t = "row"
                d[k] = (i, "row")

    # col by col
    G2 = list(zip(*G))
    for i, (c1, c2) in enumerate(list(zip(G2, G2[1:]))):
        if c1 == c2:
            to_low = i
            to_max = W - i - 2
            valid = True
            for off in range(1, min(to_low, to_max) + 1):
                valid = valid and G2[i - off] == G2[i + 1 + off]
            if valid:
                mirror = i
                t = "col"
                d[k] = (i, "col")
    s += (mirror + 1) if t == "col" else ((mirror + 1) * 100)


print(s)

s = 0
for k, pattern in enumerate(patterns):
    lines = pattern.splitlines()
    G = [[x for x in line] for line in lines]
    H = len(G)
    W = len(G[0])

    done = False

    # Bruteforce the solution,
    # Try all possibilites until match and ignore mirrors found in Part A.
    for rr in range(0, H):
        if done:
            break
        for cc in range(0, W):
            if done:
                break
            GC = deepcopy(G)
            if GC[rr][cc] == ".":
                GC[rr][cc] = "#"
            else:
                GC[rr][cc] = "."

            # row by row
            for i, (r1, r2) in enumerate(list(zip(GC, GC[1:]))):
                if r1 == r2:
                    to_low = i
                    to_max = H - i - 2
                    valid = True
                    for off in range(1, min(to_low, to_max) + 1):
                        valid = valid and GC[i - off] == GC[i + 1 + off]
                    if valid and d[k] != (i, "row"):
                        mirror = i
                        t = "row"
                        done = True
                        break

            # col by col
            G2 = list(zip(*GC))
            for i, (c1, c2) in enumerate(list(zip(G2, G2[1:]))):
                if c1 == c2:
                    to_low = i
                    to_max = W - i - 2
                    valid = True
                    for off in range(1, min(to_low, to_max) + 1):
                        valid = valid and G2[i - off] == G2[i + 1 + off]
                    if valid and d[k] != (i, "col"):
                        mirror = i
                        t = "col"
                        done = True
                        break
            if done:
                s += (mirror + 1) if t == "col" else ((mirror + 1) * 100)

print(s)
