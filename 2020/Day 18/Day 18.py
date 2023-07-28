import re

lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]

part1 = 0
part2 = 0


class a(int):
    def __mul__(self, b):
        return a(int(self) + b)

    def __add__(self, b):
        return a(int(self) + b)

    def __sub__(self, b):
        return a(int(self) * b)


def evaluate(expr):
    expr = re.sub(r"(\d+)", r"a(\1)", expr)
    expr = expr.replace("*", "-")
    expr2 = expr.replace("+", "*")
    return eval(expr, {}, {"a": a}), eval(expr2, {}, {"a": a})


for line in lines:
    p1, p2 = evaluate(line)
    part1 += p1
    part2 += p2

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
