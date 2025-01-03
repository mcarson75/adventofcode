from time import time

input = [
    l.strip().split() for l in open("input.txt", "r", encoding="utf-8").readlines()
][0][0]

start = time()


def initialize(input):
    blanks = set()
    ids = dict()
    id = 0
    index = 0

    for n in range(len(input)):
        i = int(input[n])
        if n % 2 == 0:
            ids[id] = set(range(index, index + i))
            id += 1
        else:
            blanks |= set(range(index, index + i))
        index += i

    return blanks, ids


def id_total(id):
    return id * sum(ids[id])


blanks = list()
file_ids = list()
file_indices = list()
index = 0
id = 0


for n in range(len(input)):
    i = int(input[n])
    if n % 2 == 0:
        file_ids += [id] * i
        file_indices += list(range(index, index + i))
        id += 1
    else:
        blanks += list(range(index, index + i))
    index += i

file_new = file_indices[::-1]
eff_ind = [i for i in range(len(blanks)) if blanks[i] > file_new[i]][0]
file_new[:eff_ind] = blanks[:eff_ind]
file_new = file_new[::-1]


part1 = sum([file_ids[i] * file_new[i] for i in range(len(file_ids))])

part1_time = time()

blanks, ids = initialize(input)

for id in sorted(list(ids.keys()), reverse=True):
    needed = len(ids[id])
    available = False
    for b in sorted(list(blanks)):
        new_index = set(range(b, b + needed))
        if new_index.issubset(blanks):
            available = True
            break
    if available:
        old_index = set(ids[id])
        if min(new_index) < min(old_index):
            ids[id] = set(new_index)
            blanks -= new_index
            blanks |= old_index


part2 = sum([id_total(id) for id in ids])

part2_time = time()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

print(f"Part 1 Time: {part1_time-start}s")
print(f"Part 2 Time: {part2_time-part1_time}s")
