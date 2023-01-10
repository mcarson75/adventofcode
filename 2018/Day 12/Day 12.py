input = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


get_key = lambda p, plants: "".join(
    "#" if n in plants else "." for n in range(p - 2, p + 3)
)

initial = list(input[0].split(": ")[1])
plants = set([i for i, v in enumerate(initial) if v == "#"])
input = input[2:]
input = [i.split(" => ") for i in input]
map = {k: True if v == "#" else False for k, v in input}


def get_plants(r, plants):
    diff = sum(plants)
    total = sum(plants)
    rem = None
    for _ in range(r):
        new_plants = set()
        for p in range(min(plants) - 2, max(plants) + 3):
            if map[get_key(p, plants)]:
                new_plants.add(p)
        plants = new_plants
        if (new_total := sum(plants)) - total == diff:
            total = new_total
            rem = r - _ - 1
            break
        else:
            diff = new_total - total
            total = new_total

    if rem:
        return total + rem * diff

    return sum(plants)


print(f"Part 1: {get_plants(20, plants)}")
print(f"Part 2: {get_plants(50000000000, plants)}")
