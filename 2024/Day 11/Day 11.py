from collections import defaultdict

input = [
    [int(i) for i in l.strip().split()]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
][0]

stones = {x: input.count(x) for x in set(input)}


def blink(num):
    if num == 0:
        return [1]
    numstr = str(num)
    lenstr = len(numstr)
    if lenstr % 2 == 0:
        return [int(numstr[: lenstr // 2]), int(numstr[lenstr // 2 :])]
    return [num * 2024]


def do_loop(stones):
    new_stones = defaultdict(int)
    for stone, val in stones.items():
        for res in blink(stone):
            new_stones[res] += val

    return new_stones


def do_loops(stones, blinks):
    for n in range(blinks):
        stones = do_loop(stones)
    return sum(stones.values())


part1 = do_loops(stones, 25)
part2 = do_loops(stones, 75)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
