import collections

with open("input.txt") as f:
    lines = f.read().splitlines()


G = [[x for x in line] for line in lines]
H = len(G)
W = len(G[0])

start = None
for i, r in enumerate(G):
    for j, c in enumerate(r):
        if c == "S":
            start = (i, j)


visited = []
steps = 64
news = set([start])
for step in range(0, steps):
    to_handle = news
    news = []
    for node in to_handle:
        visited.append(node)
        for rc, cc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r, c = node
            r2, c2 = (r + rc, c + cc)
            try:
                v = G[r2][c2]
                if v == "." and (r2, c2) not in news:
                    news.append((r2, c2))
            except IndexError:
                pass


print(len(news) + 1)
