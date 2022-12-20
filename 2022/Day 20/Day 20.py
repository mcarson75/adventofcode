moves = [int(l.strip()) for l in open("input.txt", "r", encoding="utf-8").readlines()]

LENGTH = len(moves)
DECRYPTION_KEY = 811589153

numbers = list(zip(range(LENGTH), moves))


def rot(a, i):
    if abs(i) > len(a):
        if i < 0:
            i = -1 * (-i % len(a))
        else:
            i %= len(a)
    return a[i:] + a[:i]


def get_coord(numbers):
    zero_i = [n[1] for n in numbers].index(0)

    return sum([numbers[(zero_i + i) % LENGTH][1] for i in [1000, 2000, 3000]])


def decode(numbers):
    for index in range(LENGTH):
        i = [n[0] for n in numbers].index(index)
        m = numbers[i][1]

        numbers = rot(numbers, i)
        this = numbers.pop(0)
        numbers = rot(numbers, m)
        numbers = [this] + numbers

    return numbers


numbers = decode(numbers)
part1 = get_coord(numbers)

print(f"Part 1: {part1}")

numbers = list(zip(range(LENGTH), [m * DECRYPTION_KEY for m in moves]))
for _ in range(10):
    numbers = decode(numbers)

part2 = get_coord(numbers)
print(f"Part 2: {part2}")
