import collections
import math
import itertools
import copy

with open("input.txt") as f:
    lines, ratings = f.read().split("\n\n")

# parsing
lines = lines.splitlines()
ratings = ratings.splitlines()

d = {}
for line in lines:
    name, rest = line.split("{")
    rules = rest.replace("{", "").replace("}", "").split(",")
    d[name] = rules

# part one
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


# part two
def permutations(intervals):
    return math.prod([1 + int(b) - int(a) for a, b in intervals.values()])


intervals = {
    "x": (1, 4000),
    "m": (1, 4000),
    "a": (1, 4000),
    "s": (1, 4000),
}


def solve(instructions, intervals, current):
    rule = instructions[current]
    val = 0

    for check in rule:
        if ">" in check:
            c, rest = check.split(">")
            v, des = rest.split(":")
            interval = intervals[c]

            if int(interval[1]) > int(v):
                intervals_copy = copy.deepcopy(intervals)
                intervals_copy[c] = (max(int(interval[0]), int(v) + 1), interval[1])

                if des == "A":
                    val += permutations(intervals_copy)
                elif des != "R":
                    val += solve(instructions, intervals_copy, des)
            intervals[c] = (interval[0], v)

        elif "<" in check:
            c, rest = check.split("<")
            v, des = rest.split(":")
            interval = intervals[c]

            if int(interval[0]) < int(v):
                intervals_copy = copy.deepcopy(intervals)
                intervals_copy[c] = (interval[0], min(int(interval[1]), int(v) - 1))

                if des == "A":
                    val += permutations(intervals_copy)
                elif des != "R":
                    val += solve(instructions, intervals_copy, des)

            intervals[c] = (v, interval[1])
        elif check == "A":
            val += permutations(intervals)
        elif check != "R":
            val += solve(instructions, intervals, check)

    return val


print(solve(d, intervals, "in"))
