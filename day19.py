with open("input.txt") as f:
    lines, ratings = f.read().split("\n\n")


lines = lines.splitlines()
ratings = ratings.splitlines()

d = {}
for line in lines:
    name, rest = line.split("{")
    rules = rest.replace("{", "").replace("}", "").split(",")
    d[name] = rules

accepted = []
rejected = []
for i, rating in enumerate(ratings):
    rating = rating.replace("{", "").replace("}", "").split(",")
    rating = {x.split("=")[0]: int(x.split("=")[1]) for x in rating}

    current = "in"
    while True:
        if current == "A":
            accepted.append(rating)
            break
        if current == "R":
            rejected.append(rating)
            break

        rule = d[current]
        for check in rule:
            if "<" in check:
                c, rest = check.split("<")
                v, des = rest.split(":")
                r = rating[c] < int(v)
                if r:
                    current = des
                    break
            elif ">" in check:
                c, rest = check.split(">")
                v, des = rest.split(":")
                r = rating[c] > int(v)
                if r:
                    current = des
                    break
            else:
                current = check

s = 0
for a in accepted:
    s += sum(a.values())

print(s)

"""
TODO: I think I need to find all paths from A to in.
Following each of these paths should give me the range for x m a x m a ss
"""
