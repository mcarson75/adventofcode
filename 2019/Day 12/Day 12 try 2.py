def least_common_multiple(x, y):
    return (x * y) // math.gcd(x, y)


def one_d_orbits(positions):
    velocities = [0] * len(positions)

    first_state = hash(tuple(velocities) + tuple(positions))
    steps = 0
    while True:
        for idx1 in range(len(positions)):
            for idx2 in range(idx1 + 1, len(positions)):
                if positions[idx1] < positions[idx2]:
                    velocities[idx1] += 1
                    velocities[idx2] -= 1
                elif positions[idx1] > positions[idx2]:
                    velocities[idx1] -= 1
                    velocities[idx2] += 1
        for x in range(len(positions)):
            positions[x] += velocities[x]

        steps += 1
        if first_state == hash(tuple(velocities) + tuple(positions)):
            return steps


def main():
    moons = read_input("input12.txt")
    cycle0 = one_d_orbits([m.x for m in moons])
    cycle1 = one_d_orbits([m.y for m in moons])
    cycle2 = one_d_orbits([m.z for m in moons])
    cycle = least_common_multiple(cycle0, least_common_multiple(cycle1, cycle2))
