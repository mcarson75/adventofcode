from collections import defaultdict
from itertools import accumulate

with open("input.txt", "r", encoding="utf-8") as f:
    change = [int(l.strip()) for l in f.readlines()]

freq = [0] + list(accumulate(change))
total = freq[-1]

freq = freq[:-1]
mods = defaultdict(list)

for i, f in enumerate(freq):
    mods[f % total].append((i, f))

min_index, min_diff, min_freq = None, None, None
for group in mods.values():
    # sort by frequency
    sorted_vals = list(sorted(group, key=lambda t: t[1]))
    for i in range(1, len(sorted_vals)):
        # calculate the difference and the index of the repetition inside the list of frequencies
        diff = sorted_vals[i][1] - sorted_vals[i - 1][1]
        index = sorted_vals[i - 1][0] if total > 0 else sorted_vals[i][0]
        freq = sorted_vals[i][1] if total > 0 else sorted_vals[i - 1][1]
        if (
            min_diff is None
            or diff < min_diff
            or (diff == min_diff and index < min_index)
        ):
            min_index = index
            min_diff = diff
            min_freq = freq

print(f"Part 1: {total}")
print(f"Part 2: {min_freq}")
