import collections

with open("input.txt") as f:
    lines = f.read().splitlines()


# Parsing and prep the data
d = collections.defaultdict(list)
types = {}
for line in lines:
    module, dests = line.split(" -> ")
    if module == "broadcaster":
        d[module] = dests.replace(" ", "").split(",")
        types[module] = ("1", "off")  # just forward
    else:
        d[module[1:]] = dests.replace(" ", "").split(",")
        types[module[1:]] = (module[0], "off")

memory = {}
for k, v in types.items():
    if v[0] == "&":
        inputs = {}
        for k2, v2 in d.items():
            if k in v2:
                inputs[k2] = "low"
        memory[k] = inputs


def handle_pulse(src, inp, receivers):
    for rec in receivers:
        if rec in types.keys():
            t, s = types[rec]
            if t == "1":
                yield (rec, d[rec], inp)
            elif t == "%":
                if inp == "low":
                    ns = "on" if s == "off" else "off"
                    types[rec] = ("%", ns)
                    out = "high" if s == "off" else "low"
                    yield (rec, d[rec], out)
            elif t == "&":
                ls = memory[rec][src]
                memory[rec][src] = inp
                if all(x == "high" for x in memory[rec].values()):
                    out = "low"
                else:
                    out = "high"
                yield (rec, d[rec], out)
        else:
            pass


lows = 0
highs = 0
for _ in range(1000):
    pulses = [("btn", ["broadcaster"], "low")]
    while pulses:
        src, dests, inp = pulses.pop(0)
        if inp == "low":
            lows += len(dests)
        else:
            highs += len(dests)
        for item in handle_pulse(src, inp, dests):
            pulses.append(item)

print(lows * highs)
