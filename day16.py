with open("input.txt") as f:
    lines = f.read().splitlines()


G = [[x for x in line] for line in lines]
H = len(G)
W = len(G[0])


def find_energized(start):
    energized = set()
    done = False
    beams = [[start]]
    news = set()
    while len(beams) > 0:
        for i, beam in enumerate(beams):
            (r, c, d) = beam[-1]
            r2 = None
            c2 = None
            if d == "r" and c < (W - 1):
                r2 = r
                c2 = c + 1

            elif d == "u" and r > 0:
                r2 = r - 1
                c2 = c

            elif d == "d" and r < (H - 1):
                r2 = r + 1
                c2 = c

            elif d == "l" and c > 0:
                r2 = r
                c2 = c - 1

            if r2 == None and c2 == None:
                del beams[i]
                continue

            tile = None
            try:
                tile = G[r2][c2]
                energized.add((r2, c2))
            except IndexError:
                del beams[i]
                continue

            new = None

            d2 = d
            if tile == "/" and d == "r":
                d2 = "u"
            if tile == "/" and d == "l":
                d2 = "d"
            if tile == "/" and d == "u":
                d2 = "r"
            if tile == "/" and d == "d":
                d2 = "l"

            if tile == "\\" and d == "r":
                d2 = "d"
            if tile == "\\" and d == "l":
                d2 = "u"
            if tile == "\\" and d == "u":
                d2 = "l"
            if tile == "\\" and d == "d":
                d2 = "r"

            if tile == "-" and d in "ud":
                d2 = "r"
                new = (r2, c2, "l")
            if tile == "|" and d in "lr":
                d2 = "u"
                new = (r2, c2, "d")

            if (r2, c2, d2) in beam:
                del beams[i]
                continue
            else:
                beam.append((r2, c2, d2))

            if new and new not in news:
                news.add(new)
                beams.append([new])
    return len(energized)


starting_pos_b = (
    [(x, -1, "r") for x in range(0, H)]
    + [(-1, x, "d") for x in range(0, W)]
    + [(x, W, "l") for x in range(0, H)]
    + [(H, x, "u") for x in range(0, W)]
)

starting_pos_a = (0, -1, "r")


print(find_energized(starting_pos_a))
print(max([find_energized(x) for x in starting_pos_b]))
