import collections
import copy

with open("input.txt") as f:
    lines = f.read().splitlines()

G = [[x for x in line] for line in lines]
H = len(G)
W = len(G[0])


# https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(path):
    pairs = [(path[i], path[(i + 1) % len(path)]) for i in range(len(path))]
    s = abs(sum(x1 * y2 - x2 * y1 for ((x1, y1), (x2, y2)) in pairs))
    return s * 0.5


def find_neighbours(grid, pos):
    r, c = pos
    neighbours = []
    for rc, cc, d in [(0, 1, "r"), (-1, 0, "u"), (1, 0, "d"), (0, -1, "l")]:
        r2 = r + rc
        c2 = c + cc
        if 0 <= r2 < W and 0 <= c2 < H:
            v = grid[r][c]
            v2 = grid[r2][c2]
            match v:
                case "|":
                    if d == "d" and v2 in ["L", "J", "|"]:
                        neighbours.append((r2, c2))
                    if d == "u" and v2 in ["7", "F", "|"]:
                        neighbours.append((r2, c2))
                case "-":
                    if d == "r" and v2 in ["J", "7", "-"]:
                        neighbours.append((r2, c2))
                    if d == "l" and v2 in ["L", "F", "-"]:
                        neighbours.append((r2, c2))
                case "L":
                    if d == "r" and v2 in ["-", "J", "7"]:
                        neighbours.append((r2, c2))
                    if d == "u" and v2 in ["|", "7", "F"]:
                        neighbours.append((r2, c2))
                case "J":
                    if d == "l" and v2 in ["-", "L", "F"]:
                        neighbours.append((r2, c2))
                    if d == "u" and v2 in ["|", "7", "F"]:
                        neighbours.append((r2, c2))
                case "7":
                    if d == "l" and v2 in ["-", "F", "L"]:
                        neighbours.append((r2, c2))
                    if d == "d" and v2 in ["|", "J", "L"]:
                        neighbours.append((r2, c2))
                case "F":
                    if d == "r" and v2 in ["-", "7", "J"]:
                        neighbours.append((r2, c2))
                    if d == "d" and v2 in ["|", "J", "L"]:
                        neighbours.append((r2, c2))
    return neighbours


def bfs(grid, start, goal):
    queue = collections.deque([[start]])
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == goal and len(path) > 1:
            return path
        for r2, c2 in find_neighbours(grid, (r, c)):
            if (r2, c2) == start and len(path) > 2:
                queue.append(path + [(r2, c2)])
            elif (r2, c2) not in path:
                queue.append(path + [(r2, c2)])


start = None
for i, row in enumerate(G):
    for j, col in enumerate(row):
        if G[i][j] == "S":
            start = (i, j)
            break

for p in ["|", "-", "L", "J", "7", "F"]:
    G2 = copy.deepcopy(G)
    G2[start[0]][start[1]] = p
    path = bfs(G2, start, start)
    if path:
        ans = (len(path) - 1) // 2
        print(ans)
        ans_two = int(shoelace(path)) - len(path) // 2 + 1
        print(ans_two)
        break
