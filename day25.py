import networkx as nx

with open("input.txt") as f:
    lines = f.read().splitlines()

G = nx.Graph()
for line in lines:
    src, dests = line.split(": ")
    dests = dests.split()
    for d in dests:
        G.add_edge(src, d)

cuts = list(nx.minimum_edge_cut(G))

G.remove_edges_from(cuts)
s = 1
for c in nx.connected_components(G):
    s *= len(c)

print(s)
