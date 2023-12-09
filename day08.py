from collections import defaultdict
import math

with open("input.txt") as f:
    lines = f.read().splitlines()


instructions = lines[0]

d = {}
for line in lines[2:]:
    c, neigh = line.split("=")
    c = c.replace(" ", "")
    d[c] = neigh.replace("(", "").replace(")", "").replace(" ", "").split(",")

done = False
c = 0
start = "AAA"
current = start
while not done:
    for ins in instructions:
        if "R" in ins:
            current = d[current][1]
        elif "L" in ins:
            current = d[current][0]

        c += 1
        if "ZZZ" in current:
            done = True

print(c)


starting_nodes = [x for x in d.keys() if x[2] == "A"]
end_nodes = [x for x in d.keys() if x[2] == "Z"]

done = False
currents = starting_nodes
res = {}
s = 0
while not done:
    for ins in instructions:
        # for all ongoing searches, check if the search is done or not
        for i, c in enumerate(currents):
            if c not in res and c in end_nodes:
                res[i] = s

        # if all searches has found a **Z node, then we are don
        if len(res) == len(starting_nodes):
            done = True
        
        # update all searches
        for i, c in enumerate(currents):
            if "R" in ins:
                currents[i] = d[c][1]
            if "L" in ins:
                currents[i] = d[c][0]

        s += 1


print(math.lcm(*res.values()))
