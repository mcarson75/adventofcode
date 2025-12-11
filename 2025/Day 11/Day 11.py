from functools import cache

lines = [
    l.strip("\n").split(": ")
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

connections = {k: set(v.split()) for k, v in lines}
connections["out"] = []


@cache
def get_paths(start, finish):
    return (
        1 if start == finish else sum(get_paths(c, finish) for c in connections[start])
    )


part1 = get_paths("you", "out")
part2 = get_paths("svr", "fft") * get_paths("fft", "dac") * get_paths("dac", "out")

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
