seats = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


def seat_id(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(seat[-3:].replace("L", "0").replace("R", "1"), 2)

    return 8 * row + col


seat_ids = set([seat_id(s) for s in seats])
available_seats = set(range(min(seat_ids), max(seat_ids) + 1))
my_seat = (available_seats - seat_ids).pop()


print(f"Part 1: {max(seat_ids)}")
print(f"Part 2: {my_seat}")
