from collections import Counter
from functools import cmp_to_key

strength_ranks = ["HC", "OP", "TP", "TOK", "FH", "FOK", "FIOK"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ranks_two = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def my_compare(a, b):
    a_cards, _ = a.split()
    b_cards, _ = b.split()

    a_type = get_type(a_cards)
    b_type = get_type(b_cards)

    if strength_ranks.index(a_type) > strength_ranks.index(b_type):
        return 1
    if strength_ranks.index(a_type) < strength_ranks.index(b_type):
        return -1

    for aa, bb in zip(a_cards, b_cards):
        if ranks.index(aa) > ranks.index(bb):
            return 1
        if ranks.index(aa) < ranks.index(bb):
            return -1


def my_compare_two(a, b):
    a_cards, _ = a.split()
    b_cards, _ = b.split()

    a_type = get_type_two(a_cards)
    b_type = get_type_two(b_cards)

    if strength_ranks.index(a_type) > strength_ranks.index(b_type):
        return 1
    if strength_ranks.index(a_type) < strength_ranks.index(b_type):
        return -1

    for aa, bb in zip(a_cards, b_cards):
        if ranks_two.index(aa) > ranks_two.index(bb):
            return 1
        if ranks_two.index(aa) < ranks_two.index(bb):
            return -1


def get_type(cards):
    cs = Counter(cards)
    if len(set(cards)) == 1:
        return "FIOK"
    if 4 in cs.values():
        return "FOK"
    if 3 in cs.values() and 2 in cs.values():
        return "FH"
    if 3 in cs.values():
        return "TOK"
    if 2 == list(cs.values()).count(2):
        return "TP"
    if 1 == list(cs.values()).count(2):
        return "OP"
    return "HC"


def get_type_two(cards):
    jokers = cards.count("J")
    cards = cards.replace("J", "")
    cs = Counter(cards)
    if jokers == 5:
        return "FIOK"
    if max(cs.values()) + jokers == 5:
        return "FIOK"
    if max(cs.values()) + jokers == 4:
        return "FOK"
    if max(cs.values()) + jokers == 3:
        if max(cs.values()) == 3:
            if 2 in cs.values() or jokers >= 1:
                return "FH"
        if max(cs.values()) == 2:
            if jokers == 2:
                return "FH"
        if 2 == list(cs.values()).count(2) and jokers > 0:
            return "FH"
        return "TOK"
    if (1 == list(cs.values()).count(2) and jokers > 0) or (
        2 == list(cs.values()).count(2)
    ):
        return "TP"
    if 1 == list(cs.values()).count(2) or jokers > 0:
        return "OP"

    return "HC"


with open("input.txt") as f:
    lines = f.read().splitlines()

res = sorted(lines, key=cmp_to_key(my_compare))

s = 0
for i, r in enumerate(res):
    bid = int(r.split()[1])
    s += (i + 1) * bid

print(s)


res_two = sorted(lines, key=cmp_to_key(my_compare_two))
s = 0
for i, r in enumerate(res_two):
    bid = int(r.split()[1])
    s += (i + 1) * bid

print(s)
