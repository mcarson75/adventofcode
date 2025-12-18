import intcode

code = [
    int(n)
    for l in open("input.txt", "r", encoding="utf-8").readlines()
    for n in l.strip().split(",")
]

code += [0] * 3000

vms = [intcode.computer(code, i) for i in range(50)]

nat = []
part1 = None
last_nat = None
count = 0
while True:
    [vm.step() for vm in vms]
    count += 1
    queue = [vm.packet for vm in vms if vm.packet_ready]
    add_255 = [q for q in queue if q[0] == 255]
    if add_255:
        nat = add_255[0][1:]
        if not part1:
            part1 = nat[-1]
    if all(vm.idle for vm in vms) and nat:
        if nat[1] == last_nat:
            part2 = nat[1]
            break
        else:
            last_nat = nat[1]
        queue += [[0] + nat]
    [vm.receive_packet(packet) for vm in vms for packet in queue]
    [vm.packet_received() for vm in vms]


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
