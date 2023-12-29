from heapq import heappush, heappop

with open("input.txt") as f:
    lines = f.read().splitlines()

G = [[int(x) for x in line] for line in lines]
H = len(G)
W = len(G[0])

start = (0, 0)
end = (H - 1, W - 1)

# cost, row, col, row_change, col_change, steps
pq = [(0, 0, 0, 0, 0, 0)]
visited = set()
ans = 0
while pq:
    cost, r, c, rc, cc, s = heappop(pq)

    if (r, c) == end:
        ans = cost - G[0][0]
        break

    if (r, c, rc, cc, s) in visited:
        continue

    visited.add((r, c, rc, cc, s))

    if s < 3 and (rc, cc) != start:
        r2 = r + rc
        c2 = c + cc

        if 0 <= r2 < H and 0 <= c2 < W:
            new_cost = cost + G[r2][c2]
            heappush(pq, (new_cost, r2, c2, rc, cc, s + 1))

    for new_rc, new_cc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (new_rc, new_cc) != (rc, cc) and (new_rc, new_cc) != (-rc, -cc):
            r2 = r + rc
            c2 = c + cc
            if 0 <= r2 < H and 0 <= c2 < W:
                new_cost = cost + G[r2][c2]
                heappush(pq, (new_cost, r2, c2, new_rc, new_cc, 1))

print(ans)


# cost, row, col, row_change, col_change, steps
pq = [(0, 0, 0, 0, 0, 0)]
visited = set()
ans = 0
while pq:
    cost, r, c, rc, cc, s = heappop(pq)

    if s >= 4 and (r, c) == end:
        ans = cost - G[0][0]
        break

    if (r, c, rc, cc, s) in visited:
        continue

    visited.add((r, c, rc, cc, s))

    if s < 10 and (rc, cc) != start:
        r2 = r + rc
        c2 = c + cc

        if 0 <= r2 < H and 0 <= c2 < W:
            new_cost = cost + G[r2][c2]
            heappush(pq, (new_cost, r2, c2, rc, cc, s + 1))

    if s >= 4 or (rc, cc) == start:
        for new_rc, new_cc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (new_rc, new_cc) != (rc, cc) and (new_rc, new_cc) != (-rc, -cc):
                r2 = r + rc
                c2 = c + cc
                if 0 <= r2 < H and 0 <= c2 < W:
                    new_cost = cost + G[r2][c2]
                    heappush(pq, (new_cost, r2, c2, new_rc, new_cc, 1))

print(ans)
