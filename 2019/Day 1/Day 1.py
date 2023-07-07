def calc_fuel(mass):
    fuel = mass // 3 - 2
    return fuel if fuel >= 0 else 0


modules = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

fuel = [calc_fuel(m) for m in modules]
total = sum(fuel)

print(f"Part 1: {total}")

while any(fuel) > 0:
    fuel = [calc_fuel(f) for f in fuel]
    total += sum(fuel)

print(f"Part 2: {total}")
