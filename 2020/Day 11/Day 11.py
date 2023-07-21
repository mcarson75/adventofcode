import numpy as np

grid = np.array(
    [list(l.strip("\n")) for l in open("input.txt", "r", encoding="utf-8").readlines()]
)

seats = {x + y * 1j: grid[y, x] for (y, x) in np.argwhere(grid == "L")}
x_range = [s.real for s in list(seats.keys())]
y_range = [s.imag for s in list(seats.keys())]


def check_bound(seat):
    if seat.real in x_range and seat.imag in y_range:
        return True
    else:
        return False


def check_adj(seats, seat, check_all=False):
    adjacent = [-1 - 1j, -1, -1 + 1j, 1j, 1 + 1j, 1, 1 - 1j, -1j]
    count = 0
    for adj in adjacent:
        if seat + adj in seats and seats[seat + adj] == "#":
            count += 1
        elif check_all and seat + adj not in seats:
            mult = 2
            while seat + mult * adj not in seats and check_bound(seat + mult * adj):
                mult += 1
            else:
                if seat + mult * adj in seats and seats[seat + mult * adj] == "#":
                    count += 1

    return count


def get_occupied(seats, num_adj, check_all=False):
    num_occupied = -1
    new_occupied = 0
    while new_occupied != num_occupied:
        num_occupied = new_occupied
        new_seats = {}
        for seat in seats.keys():
            adj = check_adj(seats, seat, check_all)
            if seats[seat] == "L" and adj == 0:
                new_seats[seat] = "#"
            elif seats[seat] == "#" and adj >= num_adj:
                new_seats[seat] = "L"
            else:
                new_seats[seat] = seats[seat]
        seats = new_seats
        new_occupied = list(seats.values()).count("#")

    return new_occupied


part1 = get_occupied(seats, 4)
print(f"Part 1: {part1}")

part2 = get_occupied(seats, 5, check_all=True)
print(f"Part 2: {part2}")
