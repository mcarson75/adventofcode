input = "739862541"

cups = [int(i) for i in input]


def do_move(array, steps):
    current = array[0]
    mn, mx = min(array), max(array)
    # Create array with the value of each key is the number following it in the array
    array_dict = dict(zip(array, array[1:] + [current]))

    for _ in range(steps):
        xyz = [array_dict[current]]
        for i in range(2):
            xyz.append(array_dict[xyz[-1]])
        dest = current - 1
        while dest < mn or dest in xyz:
            dest -= 1
            if dest < mn:
                dest = mx
        array_dict[current] = array_dict[xyz[-1]]
        array_dict[xyz[-1]] = array_dict[dest]
        array_dict[dest] = xyz[0]
        current = array_dict[current]

    return array_dict


cups_part1 = do_move(cups, 100)
labels = [cups_part1[1]]
while labels[-1] != 1:
    labels.append(cups_part1[labels[-1]])

part1 = "".join([str(i) for i in labels[:-1]])

print(f"Part 1: {part1}")

cups = [int(i) for i in input]
cups += list(range(max(cups) + 1, 1000001))

cups_part2 = do_move(cups, 10000000)
c1 = cups_part2[1]
c2 = cups_part2[c1]

print(f"Part 2: {c1*c2}")
