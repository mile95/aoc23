import collections
import itertools

with open("input.txt") as f:
    lines = f.read().splitlines()


def bfs(grid, start, goal):
    queue = collections.deque([[start]])
    seen = set([start])
    height = len(grid) + 1
    width = len(grid[0]) + 1
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == goal:
            path.remove(start)
            path.remove(goal)
            return path
        for r2, c2 in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= r2 < width and 0 <= c2 < height and (r2, c2) not in seen:
                queue.append(path + [(r2, c2)])
                seen.add((r2, c2))


G = [[x for x in line] for line in lines]

rows_to_add = []
cols_to_add = []
for r, row in enumerate(G):
    if "#" not in row:
        rows_to_add.append(r)

for c, col in enumerate(zip(*G)):
    if "#" not in col:
        cols_to_add.append(c)

galaxies = []
for r, row in enumerate(G):
    for c, item in enumerate(G[r]):
        if item == "#":
            galaxies.append((r, c))


s_part_a = 0
s_part_b = 0
for start, goal in itertools.combinations(galaxies, 2):
    path = bfs(G, start, goal)
    extra_a = 0
    extra_b = 0
    for r in rows_to_add:
        if r in [r for (r, _) in path]:
            extra_a += 1
            extra_b += 1000000 - 1
    for c in cols_to_add:
        if c in [c for (_, c) in path]:
            extra_a += 1
            extra_b += 1000000 - 1
    s_part_a += len(path) + 1 + extra_a
    s_part_b += len(path) + 1 + extra_b

print(s_part_a)
print(s_part_b)
