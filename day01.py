with open("input.txt") as f:
    input = f.read().splitlines()

s = 0
for line in input:
    numbers = [int(s) for s in line if s.isdigit()]
    number = int(str(numbers[0]) + str(numbers[-1]))
    s += number

print(s)


d = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

s = 0
for line in input:
    start_index = len(input) + 1
    start_word = ""
    end_index = 0
    end_word = ""
    for p in list(d.keys()) + list(d.values()):
        first_occ = line.find(p)
        last_occ = line.rfind(p)

        if first_occ != -1 and first_occ <= start_index:
            start_index = first_occ
            start_word = p
        if last_occ != -1 and last_occ >= end_index:
            end_index = last_occ
            end_word = p

    start_word = d[start_word] if len(start_word) > 1 else start_word
    end_word = d[end_word] if len(end_word) > 1 else end_word
    s += int(start_word + end_word)

print(s)
