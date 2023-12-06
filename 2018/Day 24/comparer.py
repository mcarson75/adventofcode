with open("output.txt", "r") as f1:
    out1 = f1.read().split("\n\n")
with open("output2.txt", "r") as f2:
    out2 = f2.read().split("\n\n")

run1 = dict()
run2 = dict()


def parse(iter):
    i, imm, inf = iter.split("\n")

    _, i = i.split(": ")
    i = int(i)

    _, imm = imm.split(": ")
    imm = set(eval(imm))

    _, inf = inf.split(": ")
    inf = set(eval(inf))

    return i, {"imm": imm, "inf": inf}


for iteration in out1:
    i, data = parse(iteration)
    run1[i] = data

for iteration in out2:
    i, data = parse(iteration)
    run2[i] = data

for i in run1:
    if run1[i] != run2[i]:
        print(f"Do not match at iteration {i}")
        print(f"Out1: {run1[i]}")
        print(f"Out2: {run2[i]}")
        break

# print("stop")
