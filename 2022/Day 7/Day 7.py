with open("input.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines()]

current_folder = ["/"]
folder_sizes = {}

for line in lines:
    if "$" in line:
        args = line.split()
        if args[1] == "cd":
            if args[2] == "/":
                current_folder = ["/"]
            elif args[2] == "..":
                current_folder.pop()
            else:
                current_folder.append(args[2])
    elif not "dir" in line:
        f_size, f_name = line.split()
        for n in range(len(current_folder)):
            folder = ("/" + "/".join(current_folder[1 : n + 1]) + "/") if n > 0 else "/"
            folder_sizes[folder] = folder_sizes.get(folder, 0) + int(f_size)

needed_space = folder_sizes["/"] - 40000000

part1 = sum([v for v in folder_sizes.values() if v <= 100000])
part2 = sorted([v for v in folder_sizes.values() if v >= needed_space])[0]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
