with open("input.txt") as f:
    lines = f.read().splitlines()


G = [[x for x in line] for line in lines]
H = len(G)
W = len(G[0])

col_G = list(zip(*G))
for k, col in enumerate(col_G):
    col = list(col)
    done = False
    while not done:
        moves = 0
        for i, c in enumerate(col):
            if c == 'O':
                for j in range(i-1, -1, -1):
                    if col[j] == '.' and '#' not in col[j:i]:
                        col[i], col[j] = col[j], col[i]
                        moves += 1
        done = moves == 0

    col_G[k] = col

G = list(zip(*col_G))

load = 0
for i, row in enumerate(G):
    load += (H - i) * row.count('O')

print(load)


G = [[x for x in line] for line in lines]
H = len(G)
W = len(G[0])


G_tmp = G
history = []
keep_looking = True
c = 0
cc = 0
iteration = 0
while iteration <= 1000000001: 
    if G in history and keep_looking:
        keep_looking = False
        iteration = 1000000000 - (1000000000 % (iteration-1))
    else:
        history.append(G)
    for d in ['N','W','S','E']:
        if d in ['W', 'E']:
            G_tmp = G
        else:
            G_tmp = list(zip(*G))
        for k, col in enumerate(G_tmp):
            if d in ['S', 'E']:
                col = list(reversed(col))
            else:
                col = list(col)
            done = False
            while not done:
                moves = 0
                for i, c in enumerate((col)):
                    if c == 'O':
                        for j in range(i-1, -1, -1):
                            if col[j] == '.' and '#' not in col[j:i]:
                                col[i], col[j] = col[j], col[i]
                                moves += 1
                    done = moves == 0
            if d in ['S', 'E']:
                G_tmp[k] = list(reversed(col))
            else:
                G_tmp[k] = list(col)
    
        if d in ['S', 'N']:
            G = list(zip(*G_tmp))
        else:
            G = G_tmp
    iteration += 1


load = 0
for i, row in enumerate(G):
    load += (H - i) * row.count('O')

print(load)

