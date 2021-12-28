pps = [l.strip().split() for l in open("input.txt", 'r', encoding='utf-8').readlines()]

no_dupe = sum([len(set(pp)) == len(pp) for pp in pps])
no_anagram = sum([len(set([''.join(sorted(p)) for p in pp])) == len(pp) for pp in pps])

print("Part 1: " + str(no_dupe))
print("Part 2: " + str(no_anagram))
