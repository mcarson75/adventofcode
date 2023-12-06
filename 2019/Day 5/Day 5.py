import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]


print(f"Part 1: {intcode.run(code, 1)}")
print(f"Part 2: {intcode.run(code, 5)}")
